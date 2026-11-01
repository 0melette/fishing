# Fishing

A shared fishing catalogue for Obsidian, Mooncake LilyGO and future device exporters: **27 species, nine tackle topics and 36 illustrations**. Freshwater yabby is included.

Edit `catalogue.json` for shared facts and `artwork/` for visuals. Each species keeps its own `checked` review date and source links. The original entries retain their October review dates; adding a species does not redate the collection. See [sources](SOURCES.md), [authoring](AUTHORING.md) and [licences](LICENSE.md).

## Use the catalogue

LilyGO consumes a pinned checkout of this repository and generates its browser/native data and artwork. Obsidian can use the same checkout:

```sh
python scripts/export_obsidian.py --vault /path/to/vault
python scripts/check.py
```

The exporter writes reference notes and images under `Hobbies/Fishing/`; it preserves generated-note frontmatter and refuses to overwrite handwritten Species/Rigs notes. It does not read, import or export personal catch records. Device installation and Xteink export are separate operations.

This public repository has no personal catches, fishing locations, private vault notes, credentials or device backups. It is a versioned reference catalogue, not a live catch-sharing service.

## Before committing or pushing

Run `python scripts/install_hooks.py` in each clone. Staged-tree and outgoing-history audits block unexpected files, private catch/location fields and likely secrets. See [publishing checks](SECURITY.md).
