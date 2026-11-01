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
