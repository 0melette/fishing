# NSW fishing guide: sources and scope

Checked against live official NSW DPIRD pages on 10 October 2026. The built-in dataset is an offline snapshot of selected public facts, manually summarised in `src/activities/apps/FishingGuideData.h`. It is not a FishSmart app export or a live integration. There is no copied fish artwork, app UI, or account data.

## Sources

- [FishSmart NSW](https://www.dpird.nsw.gov.au/fishing/recreational/resources/fishsmart-app): official app and overview of its rules, mapping and catch-log features. No documented public app API was located in the resources reviewed.
- [Saltwater limits](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/saltwater-bag-and-size-limits): all 12 saltwater entries, including grouped limits and possession rules. Snapshot uses the live webpage, not the older printed guide. Dusky flathead possession is 10 on this page at review time.
- [Freshwater limits](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/freshwater-bag-and-size-limits): four freshwater entries; eel possession is explicitly 10 rather than doubling the daily bag. Murray cod's seasonal closure and Copeton/Blowering exceptions are retained.
- [How to measure fish](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/measure): finfish measurement and shrinkage guidance, paraphrased for the reference page.
- [Recreational fishing](https://www.dpird.nsw.gov.au/fishing/recreational): fishing-fee requirement, with exemptions to check in official guidance.
- [Interactive map](https://www.dpird.nsw.gov.au/fishing/recreational/resources/interactive-map-for-recreational-fishers): current closure, marine-zone, and other location layers. QR link only; this firmware does not cache maps or assess whether a fishing location is open.
- [Eastern blue groper prohibition](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/new-blue-groper-fishing-rule-changes): additional cross-check of the no-take entry, including colour variants.

## Review rules for updates

Treat a dash in the official length column as “Not specified,” not a blanket statement that other restrictions never apply. Keep combined limits attached to the named species group. Preserve upper-size limits, no-take status, boat limits, seasonal exceptions, and possession exceptions. Never derive possession limits by blindly doubling daily bags.

Change the checked date only after re-reading the live sources and reviewing all entries. If official sources conflict, record the discrepancy and verify the current rule before updating the reference. Do not infer permission to keep a fish from a single size/bag value.

Use explicit source attribution and paraphrased factual summaries. Artwork and bulk spatial-data reuse need separate source-specific rights review; they are not included in this version. The spatial portal's published licence description is ambiguous, so no map dataset licence is assumed.

## Practical guide and illustrations (10 Oct 2026)

The footer and repeated rule CTA were removed from everyday screens. Legal data and official source QR codes remain separately accessible. Advice is a set of starting suggestions, not a forecast or a claim that a particular location is open. Location suggestions describe habitat types, rather than naming access points or giving navigation coordinates.

- [DPIRD species catalogue](https://www.dpird.nsw.gov.au/fishing/fish-species): distinguishing features, scientific names and habitats. Individual entries checked: Australian salmon, yellowfin bream, dusky flathead, blue groper, luderick, mulloway, sand whiting, trevallies, snapper, tailor, tarwhine, yellowtail kingfish, golden perch, eels and Murray cod.
- [NSW saltwater fishing guide](https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0012/600222/NSWDPIRD-Saltwater-Fishing-Guide-2024.pdf): bait suggestions. Its older legal tables do not replace the current website rules.
- [NSW freshwater fishing guide 2025-26](https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0011/600221/NSWDPIRD-Freshwater-Fishing-Guide-2024.pdf): eel/catfish bait, habitats and handling/rig principles. Eel-tailed catfish use worms or small yabbies; the user's prawn example was not copied as a verified species-specific recommendation.
- [GoFishing Great Lakes](https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0008/1387646/16867-GoFishingGuide_GreatLakesWeb-2024.pdf): flathead, whiting and luderick techniques and seasonal suggestions. Local seasonal observations are presented as starting points, not NSW-wide guarantees.
- [GoFreshwaterFishing Wyangala](https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0004/1505641/GoFishing_WyangalaWeb-2024.pdf): perch/cod structure, bait, rigs and catfish worm presentation.
- [Circle hooks](https://www.dpird.nsw.gov.au/dpi/fishing/recreational-fishing/responsible-fishing/catch-and-release/circle-hooks-benefits-and-tips): non-offset circle hooks, exposed point, steady winding rather than striking.

Dawn/dusk, tidal flow, lightly weighted bait presentation and the suggested starting leader length are editorial fishing suggestions. They are not measured bite predictions or FishSmart live data. Protected blue groper has observation/release advice, with no bait recommendation.

### Eel-tailed catfish rules

The current [freshwater limits](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/freshwater-bag-and-size-limits) specify 30 cm, 5 daily/10 possession in eastern and listed western dams, and 2 daily/4 possession in eastern rivers. Western rivers and unlisted western dams are no-take. Listed western catfish dams: Ben Chifley, Burrendong, Chaffey, Copeton, Keepit, Pindari, Split Rock, Windamere and Wyangala. The card explicitly restricts its dam/rivers limits to permitted waters.

### Generated assets

26 original illustrations were generated with the built-in imagegen tool, one call per species. They are schematic aids, not official DPIRD images or a certified taxonomic key. The bream illustration is yellowfin bream, explicitly labelled in its identifying text. Monochrome cannot preserve diagnostic colours. Check fins, shape and text; uncertain catches need a more complete reference.

Final project assets: `assets/fishing-guide/*.png`, each 360 x 180, 1-bit, no dithering. Firmware embeds 8,100 bytes per fish (210,600 bytes total), with no image decoding or SD dependency. Pixels use the orientation-aware renderer because its raw image function does not rotate bitmap bits.

The subject/prompt manifest is `artwork/sources.json`. For the 25 main images the exact prompt was:

> Use case: scientific-educational. Asset: identification aid for monochrome Xteink e-paper. One {subject}, full body strict left-facing lateral profile on pure white. Anatomically plausible black ink contours and sparse coarse hatching, no grey gradients, no dense dots, no shadow, no environment, no text or labels. Wide composition with white margin, readable at 360x180 pixels. Preserve species diagnostic silhouette and fins.

Catfish used the same visual requirements with explicit four pairs of barbels, a blunt head, scaleless body, short spined first dorsal, continuous second dorsal/anal/tail fin and no forked tail. Original generated files remain at the provenance paths recorded in the manifest; runtime and default rebuilding depend only on the committed optimized PNGs. `scripts/fishing-images.py` repacks those PNGs. `--sources` reconverts originals when available. `scripts/fishing-preview.py` rebuilds the preview from firmware content.

Exact first catfish prompt:

> Use case: scientific-educational. Asset type: monochrome fish reference illustration for an 800x480 Xteink e-paper device. Primary request: one anatomically accurate Australian freshwater eel-tailed catfish, Tandanus tandanus, shown full body in strict left-facing lateral profile, isolated on pure white. Broad rounded blunt head; four pairs of barbels around mouth; scaleless sturdy body narrowing to an eel-like tapering rounded tail; short tall first dorsal fin behind head with a spine; long second dorsal fin continuous around the tail into anal fin; pectoral fins with stout leading spines. Clear silhouette and readable fin outlines. Black ink line art with sparse coarse hatching, no grey gradients, no dense dots, no background, no shadow, no text or labels, no decorative objects, no colour. Wide landscape composition, fish fills 85% width with clear white margin, optimized to remain legible at 360x180 pixels. Do not draw a forked caudal fin or a generic American channel catfish.

## Illustrated tackle and tide guides

Nine original editable SVG diagrams now cover circle/J/long-shank hooks; stem/waggler/cork floats; ball/bean, split-shot and end sinkers; barrel/snap swivels and leader; running-sinker, float and paternoster rigs; bait presentation/landing net; and a tide-height curve. These are code-authored instructional schematics rather than generated artwork. The hook diagram shows the difference in point direction; rig drawings show component order and attachment positions. They do not depict knots or prescribe a hook count beyond the illustrated single-hook examples.

The [DPIRD saltwater guide, knots and rigs section](https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0012/600222/NSWDPIRD-Saltwater-Fishing-Guide-2024.pdf) supports the running-sinker/swivel arrangement, end-weight paternoster, and float/split-shot setup. Hook-setting advice follows the previously linked DPIRD circle-hook resource. General weight and leader suggestions are editorial starting points.

Tide concepts were checked against the [Bureau of Meteorology's tides and sea-level guide](https://www.bom.gov.au/resources/learn-and-explore/marine-knowledge-centre/tides-and-sea-level): high/low levels, changing height, spring/neap ranges and flood/ebb/slack flow. The [NOAA tidal-current FAQ](https://tidesandcurrents.noaa.gov/faq.html) supports the distinction between high/low water and slack current. The curve is schematic, with no calendar, time interval or local forecast implied. Tide height and surf/swell are different information. Actual local predictions remain available from [BOM tide predictions](https://www.bom.gov.au/australia/tides/).

Editable sources and final PNGs: `artwork/diagrams/`. Each diagram is 720 x 240, 1-bit with no dithering; nine packed images use 194,400 bytes of flash. Diagram labels use 20 px text and 3 px strokes. `scripts/fishing-diagrams.mjs` renders the SVGs with Playwright; `scripts/fishing-diagrams-pack.py` packs the committed PNGs for firmware. Rendering uses orientation-aware pixels, with no SD dependency or background work.

Every guide opens on Diagram; Left/Right or Confirm switches Diagram/Advice. Back retains the selected guide, and reopening resets to Diagram. Nine topics are available across the guide list's two pages.

## Freshwater expansion (10 Oct 2026)

Freshwater now has 14 entries. Added European carp, bony bream, barramundi, Australian bass, rainbow trout, brown trout, silver perch, redfin perch and estuary perch, with nine generated illustrations using the common prompt above and subjects recorded in the manifest.

Current [NSW freshwater limits](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/freshwater-bag-and-size-limits) underpin shared bass/perch bags, seasonal river no-take, trout water classes and stream seasons, listed-dam-only silver perch and other native finfish limits. Trout spawning limits shown are conditional on May to the June long weekend; October to April uses fly/lure limits. Local exceptions still apply.

[Bony bream identification and diet](https://australian.museum/learn/animals/fishes/bony-bream-nematalosa-erebi/) support the deep body, dorsal filament and mainly algae/detritus diet; this is an observation entry rather than a promised bait target. Freshwater bream here means bony bream, not coastal yellowfin bream. [Barramundi range](https://australian.museum/learn/animals/fishes/barramundi-lates-calcarifer-bloch-1790/) and [NSW aquaculture guidance](https://www.dpird.nsw.gov.au/dpi/fishing/aquaculture/resources/publications/species2/freshwater/barramundi) support its northern-Australia/authorised-stocked-venue framing. No NSW wild-catch limit is invented for barramundi.

The DPIRD species catalogue entries for [bass](https://www.dpird.nsw.gov.au/fishing/fish-species/species-list/australian-bass), [rainbow trout](https://www.dpird.nsw.gov.au/fishing/fish-species/species-list/rainbow-trout), [brown trout](https://www.dpird.nsw.gov.au/fishing/fish-species/species-list/brown-trout), [silver perch](https://www.dpird.nsw.gov.au/fishing/fish-species/species-list/silver-perch) and [estuary perch](https://www.dpird.nsw.gov.au/fishing/fish-species/species-list/estuary-perch) inform identification and habitat. Bait, timing and rig cards are practical starting suggestions rather than catch predictions.

[Official redfin pest FAQ](https://www.dpird.nsw.gov.au/dpi/biosecurity/aquatic-biosecurity/aquatic-pests-and-diseases/freshwater-pests/freshwater-finfish/redfin-perch/commonly-asked-questions-by-recreational-anglers-regarding-pest-listing-of-redfin-perch-in-nsw-legislation) supports no return, no live possession and no redfin bait. [Inland gear rules](https://www.dpird.nsw.gov.au/fishing/recreational/fishing-rules-and-regs/perm-prohib-freshwater) prohibit live finfish as inland bait.

## Freshwater yabby · 1 November 2026

The entry retains its own review date and official source URLs. Its original owner-directed imagegen illustration is in artwork/creatures/yabby.png. The older 26 records retain their earlier review date.
