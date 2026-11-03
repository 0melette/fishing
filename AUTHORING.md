# Add an entry

1. Choose a stable `id` and artwork key. Verify identity and region; keep freshwater yabbies separate from saltwater nippers.
2. Add the existing identification, practical-advice and rule fields. Record official source links and the actual entry-level review date. Preserve combined bags, seasonal exceptions and regional applicability.
3. Add a separate creature PNG and provenance in `artwork/sources.json`. Prefer a clean background and visible anatomy; inspect generated illustrations against reliable references. Do not substitute an illustration for definitive identification.
4. Run `python scripts/check.py` and review the change. The validator's expected count is deliberately reviewed alongside additions.
5. Update/pin the consuming app checkout, run its exporter and tests, then import reference notes. An installed board needs its own backed-up update.

LilyGO creature packing is monochrome at up to 128×76; diagrams allow 140×76. Gradients and thin strokes may disappear. Keep source art and inspect the native-size result.

Personal catches and locations belong in private stores outside this repository. Xteink export and invertebrate count/measurement controls remain separate implementation work.

## Detailed tackle notes

Keep short device summaries in the existing topic fields. `note_sections` holds longer reference explanations; `note_assets` lists companion files from `artwork/diagrams/` for the Obsidian exporter. Species `rig_links` connects a phrase to an existing topic heading. Escape image-size and alias pipes in Markdown table cells.

Sinker rows pair CC0 real-tackle photographs with separate 140×76 monochrome schematics. Photo PNGs show selected views of the source photographs; their credits and reuse terms stay with each file. Credits and source links are in `artwork/sources.json` and the exported note. Native JSON companions use the LilyGO `w`, `h`, `pixels` format with row-padded, most-significant-bit-first black pixels. These assets are prepared for device integration; adding them does not install or select them in an app.
