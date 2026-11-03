"""Validate public catalogue, artwork and absence of local/private payloads."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'catalogue.json').read_text());assert data['schema_version']==1
ids=[f['id'] for f in data['species']];assert len(ids)==len(set(ids)) and len(ids)==27
for f in data['species']:
 for key in ['id','name','image','checked','identify','source','length','daily','possession','conditions']:assert f.get(key) is not None,(f['id'],key)
 assert 0<=f['source']<len(data['sources'])
 assert (root/'artwork/creatures'/(f['image']+'.png')).is_file()
for t in data['topics']:assert (root/'artwork/diagrams'/(t['diagram']+'.png')).is_file()
manifest=json.loads((root/'artwork/sources.json').read_text())
for item in manifest.values():assert (root/item['file']).is_file()
for p in root.rglob('*'):
 if '.git' in p.parts or not p.is_file() or p.suffix not in ['.json','.md','.py','.yml']:continue
 s=p.read_text();assert ('/'+'Users/') not in s and ('/dev/'+'cu.') not in s,'Local machine path: '+str(p)
for key in ['catches','catch_logs','locations','credentials','tokens','device_state']:assert key not in data
print('PASS: 27 species, 9 tackle topics, 36 illustrations; public catalogue/artwork checks')

# Export only reference content; private catch data is not an input or output.
import tempfile,subprocess,sys
with tempfile.TemporaryDirectory() as folder:
 vault=Path(folder);private=vault/'private-catches.json';private.write_text('{"test":"leave unchanged"}')
 subprocess.run([sys.executable,str(root/'scripts/export_obsidian.py'),'--vault',str(vault)],check=True)
 assert private.read_text()=='{"test":"leave unchanged"}'
 assert len(list((vault/'Hobbies/Fishing/Species').glob('*.md')))==27
 expected_pngs = {f['image']+'.png' for f in data['species']}
 expected_pngs.update(name for t in data['topics'] for name in t.get('note_assets', []) if name.endswith('.png'))
 assert {p.name for p in (vault/'Hobbies/Fishing/Assets').glob('*.png')} == expected_pngs
 for t in data['topics']:
  for name in t.get('note_assets', []):
   assert (vault/'Hobbies/Fishing/Assets'/name).read_bytes() == (root/'artwork/diagrams'/name).read_bytes()
 assert '1 Nov 2026' in (vault/'Hobbies/Fishing/Species/Freshwater yabby.md').read_text()
 assert '10 Oct 2026' in (vault/'Hobbies/Fishing/Species/Dusky flathead.md').read_text()
print('PASS: fresh-vault export, entry review dates and private-catch sentinel unchanged')
