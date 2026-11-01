#!/usr/bin/env python3
"""Import the Mooncake LilyGO/Xteink fishing snapshot into Obsidian. Never uploads devices."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--source', type=Path, default=ROOT/'catalogue.json')
p.add_argument('--vault', type=Path, required=True)
p.add_argument('--assets', type=Path, default=ROOT/'artwork/creatures')
a = p.parse_args()
vault = a.vault.resolve()
assert vault.is_dir(), "Vault not available"
raw = a.source.read_text()
prefix = 'window.FISHING_DATA = '
if a.source.suffix == '.json':
    data = json.loads(raw)
elif raw.startswith(prefix):
    data = json.loads(raw[len(prefix):].strip().removesuffix(';'))
else:
    raise SystemExit('Expected catalogue JSON or FISHING_DATA assignment')
assert data['species'] and data['topics'], 'Empty catalogue'
ids = [f.get('id', f['image']) for f in data['species']]
assert len(set(ids)) == len(ids), 'Duplicate species ID'
for f in data['species']:
    assert all(k in f for k in ['name','image','source','identify','length','daily','possession','conditions'])
    assert 0 <= f['source'] < len(data['sources']), 'Invalid source index'
root = vault / 'Hobbies/Fishing'
def safe(s):
    return s.replace('/', ' - ').replace(':', ' -')
def write(folder, title, body, checked):
    path = root / folder / (safe(title) + '.md')
    old = path.read_text() if path.exists() else ''
    if old and 'generated_by: sync_fishing_notes.py' not in old:
        raise SystemExit(f'Refusing to overwrite handwritten note: {path}')
    if old.startswith('---\n'):
        front = old.split('---\n',2)[1]
        front = re.sub(r'^source_checked:.*$', 'source_checked: '+json.dumps(checked), front, flags=re.M)
    else:
        front = 'one_sentence: '+json.dumps(title+' reference from the Mooncake fishing guide.')+'\ngenerated_by: sync_fishing_notes.py\nsource_checked: '+json.dumps(checked)+'\ncssclasses:\n  - fishing-field-guide\n'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('---\n'+front+'---\n\n'+body+'\n\n[[Acting/Fishing Home|← Fishing home]]\n')
for f in data['species']:
    source = data['sources'][f['source']]
    checked = f.get('checked', data['checked'])
    picture = ''
    if a.assets:
        art = a.assets / (f['image']+'.png')
        assert art.is_file(), art
        dest = root/'Assets'/art.name
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(art,dest)
        picture = '![[Hobbies/Fishing/Assets/'+art.name+'|320]]\n\n'
    body = picture+f"**Identify:** {f['identify']}\n\n## Fishing notes\n\n**Bait:** {f['bait']}\n\n**Where:** {f['where']}\n\n**When:** {f['when']}\n\n**Rig:** {f['rig']}\n\n## Rules · {checked}\n\n| Length | Daily bag | Possession |\n| --- | --- | --- |\n| {f['length']} | {f['daily']} | {f['possession']} |\n\n**Conditions:** {f['conditions']}\n\n[Official rules]({source}). Check current rules and local closures before fishing."
    if f.get('source_urls'):
        body+='\n\n'+' · '.join('[Source '+str(i+1)+']('+url+')' for i,url in enumerate(f['source_urls']))
    write('Species', f['name'], body, checked)
for t in data['topics']:
    write('Rigs', t['title'], f"{t['caption']}\n\n## {t['leftTitle']}\n\n{t['left']}\n\n## {t['rightTitle']}\n\n{t['right']}", data['checked'])
(root/'Data/mooncake-fishing.json').write_text(json.dumps({'provenance': {'imported_from': str(a.source), 'sha256': hashlib.sha256(raw.encode()).hexdigest(), 'rules_checked': data['checked'], 'direction': 'Reviewed catalogue to Obsidian; per-entry dates retained; no device upload'}, 'guide': data}, indent=2)+'\n')
print(f"Imported {len(data['species'])} species and {len(data['topics'])} tackle topics; per-entry rule dates retained")
