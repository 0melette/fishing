"""Exercise privacy gates with synthetic fixtures, never real private records."""
import json,shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class AuditTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.repo=Path(self.tmp.name)
  for name in ['catalogue.json','artwork']:
   source=ROOT/name;target=self.repo/name
   if source.is_dir():shutil.copytree(source,target)
   else:shutil.copy2(source,target)
  (self.repo/'README.md').write_text('Public fishing reference.\n')
  self.git('init','-b','main');self.git('config','user.email','fixture@example.invalid');self.git('config','user.name','Audit fixture');self.git('add','.')
 def tearDown(self):self.tmp.cleanup()
 def git(self,*args):return subprocess.check_output(['git','-C',str(self.repo),*args],stderr=subprocess.PIPE).decode().strip()
 def audit(self,*args,input=None):return subprocess.run([sys.executable,str(ROOT/'scripts/audit_public.py'),'--repo',str(self.repo),*args],input=input,capture_output=True,text=True)
 def test_valid_reference_passes(self):self.assertEqual(self.audit('--staged').returncode,0)
 def test_unrelated_note_blocked(self):
  (self.repo/'personal-note.md').write_text('Unrelated note.');self.git('add','.');r=self.audit('--staged');self.assertNotEqual(r.returncode,0);self.assertIn('unrelated/unapproved path',r.stderr)
 def test_private_field_blocked(self):
  p=self.repo/'catalogue.json';d=json.loads(p.read_text());d['species'][0]['latitude']=0;p.write_text(json.dumps(d));self.git('add','.');r=self.audit('--staged');self.assertNotEqual(r.returncode,0);self.assertIn('private/credential field',r.stderr)
 def test_staged_secret_blocked_even_if_working_copy_clean(self):
  p=self.repo/'README.md';p.write_text('/'+'Users/fixture/private-note.md');self.git('add','README.md');p.write_text('Clean working copy.');r=self.audit('--staged');self.assertNotEqual(r.returncode,0);self.assertIn('local user path',r.stderr)
 def test_token_blocked_without_echoing_value(self):
  secret='gh'+'p_'+'A'*36;(self.repo/'README.md').write_text(secret);self.git('add','.');r=self.audit('--staged');self.assertNotEqual(r.returncode,0);self.assertIn('GitHub token',r.stderr);self.assertNotIn(secret,r.stderr)
 def test_deleted_leak_in_outgoing_history_blocked(self):
  (self.repo/'personal-note.md').write_text('Synthetic unrelated note.');self.git('add','.');self.git('commit','-m','Bad fixture');(self.repo/'personal-note.md').unlink();self.git('add','-A');self.git('commit','-m','Remove fixture');sha=self.git('rev-parse','HEAD');self.assertEqual(self.audit('--tree','HEAD').returncode,0)
  r=self.audit('--pre-push',input='refs/heads/main '+sha+' refs/heads/main '+'0'*40+'\n');self.assertNotEqual(r.returncode,0);self.assertIn('personal-note.md',r.stderr)
if __name__=='__main__':unittest.main()
