#!/usr/bin/env python3
"""Audit Git trees, not working files, before publishing the public catalogue."""
import argparse,json,re,subprocess,sys
from pathlib import Path

DOCS={'README.md','AUTHORING.md','SOURCES.md','LICENSE.md','SECURITY.md','.gitignore','.github/workflows/check.yml'}
CODE={'scripts/check.py','scripts/export_obsidian.py','scripts/audit_public.py','scripts/test_audit.py','scripts/install_hooks.py','.githooks/pre-commit','.githooks/pre-push'}
BLOCKED_KEYS={'catches','catch_logs','catch_history','catch_records','device_state','credentials','password','access_token','refresh_token','client_secret','private_key','latitude','longitude','gps','locations'}
PATTERNS=[('local user path',re.compile('/'+'Users/|/'+'home/[a-zA-Z0-9_.-]+/')),('private key',re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),('GitHub token',re.compile(r'(?:gh[pousr]_|github_pat_)[A-Za-z0-9_]{20,}')),('cloud access key',re.compile(r'AKIA[A-Z0-9]{16}')),('bearer secret',re.compile(r'(?i)Bearer\s+[A-Za-z0-9_.-]{24,}'))]

def git(repo,*args):
 return subprocess.check_output(['git','-C',str(repo),*args],stderr=subprocess.PIPE)

def private_keys(value,path=''):
 if isinstance(value,dict):
  for key,item in value.items():
   if key.lower() in BLOCKED_KEYS:raise ValueError('private/credential field '+path+key)
   private_keys(item,path+key+'.')
 elif isinstance(value,list):
  for item in value:private_keys(item,path)

def audit(repo,tree):
 entries={}
 for raw in git(repo,'ls-tree','-r','-z',tree).split(b'\0'):
  if not raw:continue
  metadata,name=raw.split(b'\t',1);mode,kind,sha=metadata.decode().split();name=name.decode()
  if mode not in {'100644','100755'} or kind!='blob':raise ValueError('unsupported symlink/submodule: '+name)
  entries[name]=sha
 def read(name):
  if name not in entries:raise ValueError('missing '+name)
  return git(repo,'cat-file','blob',entries[name])
 data=json.loads(read('catalogue.json'));private_keys(data)
 ids=[item['id'] for item in data['species']]
 if not ids or len(ids)!=len(set(ids)):raise ValueError('empty or duplicate species IDs')
 creatures={item['image'] for item in data['species']};diagrams={item['diagram'] for item in data['topics']}
 assets={'artwork/creatures/'+key+'.png' for key in creatures}
 assets|={'artwork/diagrams/'+key+ext for key in diagrams for ext in ['.png','.svg']}
 allowed=DOCS|CODE|assets|{'catalogue.json','artwork/sources.json'}
 for name in entries:
  if name not in allowed:raise ValueError('unrelated/unapproved path: '+name)
  raw=read(name)
  if len(raw)>12*1024*1024:raise ValueError('unexpected file size: '+name)
  if name.endswith('.png'):
   if not raw.startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('not a PNG: '+name)
   continue
  text=raw.decode('utf8')
  for label,pattern in PATTERNS:
   if pattern.search(text):raise ValueError(label+' in '+name)
  if name.endswith('.json'):private_keys(json.loads(text))
  if name.endswith('.svg') and re.search(r'(?i)(?:<!ENTITY|<!DOCTYPE|(?:href|src)\s*=\s*["\'](?:https?:|file:|data:))',text):raise ValueError('external/embedded SVG content: '+name)
 for name in {'artwork/creatures/'+key+'.png' for key in creatures}:read(name)
 for key in diagrams:read('artwork/diagrams/'+key+'.png')
 return len(entries)

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path.cwd());p.add_argument('--staged',action='store_true');p.add_argument('--pre-push',action='store_true');p.add_argument('--tree',default='HEAD');a=p.parse_args()
 trees=[]
 if a.pre_push:
  for line in sys.stdin:
   local_ref,local_sha,remote_ref,remote_sha=line.split()
   if set(local_sha)=={'0'}:continue
   if set(remote_sha)=={'0'}:commits=git(a.repo,'rev-list',local_sha).decode().splitlines()
   else:commits=git(a.repo,'rev-list',remote_sha+'..'+local_sha).decode().splitlines()
   trees.extend(commits or [local_sha])
 elif a.staged:trees=[git(a.repo,'write-tree').decode().strip()]
 else:trees=[a.tree]
 try:
  for tree in dict.fromkeys(trees):count=audit(a.repo,tree)
 except (ValueError,KeyError,UnicodeDecodeError,json.JSONDecodeError) as error:
  print('PUBLIC FISHING AUDIT BLOCKED: '+str(error),file=sys.stderr);return 1
 print('Public fishing audit passed:',len(set(trees)),'staged tree/outgoing commit(s).');return 0
if __name__=='__main__':sys.exit(main())
