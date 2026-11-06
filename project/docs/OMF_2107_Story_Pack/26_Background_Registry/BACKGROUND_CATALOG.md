# One Must Fall 2107 — Shared Background Catalog v1.0

**Source:** Story Pack v2.6, active 12 pilot campaigns (Ari in 6 files) plus Christian's independent subplot. All previous manuscript files are preserved; new active revisions refer to this registry.

## Code syntax and production contract

`[BG: BG-ARE-MAIN@DAY]` references a **shared background state**. `BG-ARE-MAIN` is the location family; `@DAY` is a lighting/state variant, not a new location. `BASE` is neutral. The variants `ARCHIVAL`, `DAY`, `EVENING`, `NIGHT`, `SUNSET`, `EMERGENCY` and `AFTERMATH` share one layout and camera. Backgrounds are 16:9 environment-only plates. Characters, HARs, trophy labels, UI and moving crowds belong on separate layers.

- `BG: X -> Y`: successive cuts in the same scene; not two simultaneous backgrounds.
- `BG: X | Y`: one of two alternate locations; production must choose from the rendered condition.
- `STAGING PROVISIONAL`: no explicit location slugline in the script. Background is an editorial staging suggestion; these assignments must be reviewed by the script editor before image production (they are not verified scene locations).
- `VERIFY LOCATION ALIAS`: source uses a distinct or weakly specified room and alias may need a unique asset after art-direction review.
- **Don't use protagonist identity to duplicate locations.** The same arena, atrium and garden codes are reused across campaigns. Branches choose which scene is rendered, not which background name exists.
- **Status:** all bracket wins, romance options, Devroe revelations and Nova chronology remain untouched. This operation adds art-direction references only. No backgrounds have been generated.

## Files

- `background_registry.json` — complete catalog, sources, variant list, prompt text, review markers.
- `background_registry.csv` — sortable location catalog.
- `background_states.csv` — each concrete `BG-CODE@STATE` plus its image-generation prompt.
- `scene_background_bindings.csv` — source line/scene -> new script -> background code mapping.
- `optional_scene_locations.csv` — reference suggestions for historical optional scene-card files (not rewritten as active scripts).
- `test_background_registry.py` — ref-integrity test for the active screenplay files.

## Location registry

| Code | Name | States | Script scenes | Status |
|---|---|---|---:|---|
| `BG-ARE-ENTRY` | Arena arrival and residential circulation | BASE, EVENING, NIGHT | 5 | source-mapped |
| `BG-ARE-HALL` | Hall of champions / veterans memorial exhibits | BASE, DAY, NIGHT | 7 | source-mapped |
| `BG-ARE-LOUNGE` | Athlete lounge and cafeteria | BASE, DAY, EVENING, NIGHT | 6 | source-mapped |
| `BG-ARE-MAIN` | Main tournament combat arena | BASE, DAY, NIGHT | 80 | source-mapped |
| `BG-ARE-MED` | Tournament medical and recovery facilities | BASE, DAY | 6 | source-mapped |
| `BG-ARE-PREPTUN` | Arena preparation and broadcast tunnels | BASE, NIGHT | 8 | source-mapped |
| `BG-ARE-RESEARCH` | Research combat enclosure / Nova boss battleground | BASE, EMERGENCY, NIGHT | 10 | source-mapped |
| `BG-ARE-SIM` | Robot simulation/calibration stage | BASE, EVENING, NIGHT | 3 | source-mapped |
| `BG-ARE-TRAIN` | HAR practice arena and training floor | AFTERMATH, BASE, DAY, EMERGENCY, EVENING, NIGHT, SUNSET | 20 | source-mapped |
| `BG-ARE-WALK` | Arena concourse and official results hall | BASE, EVENING, NIGHT | 10 | source-mapped |
| `BG-COR-BOARD` | WAR board executive chamber and office | BASE, DAY, NIGHT | 8 | source-mapped |
| `BG-COR-CALL` | Secure office private call booth | NIGHT | 1 | source-mapped |
| `BG-COR-LICENSING` | WAR procurement / licensing / supervision public offices | DAY | 1 | source-mapped |
| `BG-EPI-CIVIL` | Post-crisis civic workshop and future gallery | AFTERMATH | 1 | source-mapped |
| `BG-EPI-RECOVERY` | Aftermath recovery atrium and clinics | AFTERMATH, NIGHT | 2 | source-mapped |
| `BG-EXT-COLONY-CONSTRUCTION` | Ganymede colony construction montage | BASE | 1 | source-prose-mapped |
| `BG-EXT-GANYMEDE` | Ganymede colony and icy exterior | BASE | 1 | source-mapped |
| `BG-EXT-STATION` | Orbital anniversary complex exterior | BASE, NIGHT | 2 | source-mapped |
| `BG-HIS-ARENA97` | 2097 combat tournament arena | ARCHIVAL | 1 | source-prose-mapped |
| `BG-HIS-LAB97` | 2097 destroyed Nova laboratory | ARCHIVAL | 1 | source-prose-mapped |
| `BG-INV-ARCHIVE` | Records, safety and independent evidence archives | BASE, DAY, NIGHT | 10 | source-mapped |
| `BG-INV-CONFERENCE` | Neutral meeting / investigation room | BASE, DAY, EVENING, NIGHT | 11 | source-mapped |
| `BG-INV-COUNSEL` | Counsel and ethics office | BASE, EVENING, NIGHT | 5 | source-mapped |
| `BG-INV-DEPOSITION` | Depositions and authenticated evidence room | BASE, DAY, EVENING | 5 | source-mapped |
| `BG-INV-DESK` | Private investigation, editorial and research desks | DAY, EMERGENCY, NIGHT | 4 | source-mapped |
| `BG-INV-FORENSIC` | Forensic evidence lab and inspection room | DAY, NIGHT | 3 | source-mapped |
| `BG-INV-HEARING` | Independent hearing / tribunal / public oversight | AFTERMATH, DAY, NIGHT | 13 | source-mapped |
| `BG-LAB-NEURAL-CLINIC` | NII clinical consultation and research examination | BASE, DAY, EVENING, NIGHT | 4 | source-mapped |
| `BG-LAB-NEURAL-EXHIBIT` | Public neural-interface exhibit / showroom | NIGHT | 2 | source-mapped |
| `BG-LAB-NEURAL-TEST` | Neural diagnostics and integration labs | BASE, NIGHT | 7 | source-mapped |
| `BG-LAB-NOVA-CHAMBER` | Nova containment chamber and mechanical cradle | BASE, EMERGENCY, NIGHT | 8 | source-mapped |
| `BG-LAB-NOVA-RELAY` | Neural command relay and executive gateway | BASE, DAY, EMERGENCY, NIGHT | 12 | source-mapped |
| `BG-LAB-RESTRICTED` | Restricted research laboratory and records room | BASE, EVENING, NIGHT | 9 | source-mapped |
| `BG-LAB-REVIEW` | Independent scientific review lab | AFTERMATH, BASE, DAY, EVENING | 6 | source-mapped |
| `BG-LOC-ARENA-VIEWING-TERRACE` | Arena Viewing Terrace | NIGHT | 1 | source-mapped |
| `BG-RES-ARI` | Ari private residential quarters | BASE | 1 | source-mapped |
| `BG-RES-CHRISTIAN` | Christian temporary room | NIGHT | 1 | source-mapped |
| `BG-RES-GENERIC` | Pilot apartments, guest suites and balcony | BASE, EVENING, NIGHT | 6 | source-mapped |
| `BG-RES-LYRA` | Lyra private preparation suite | BASE | 2 | source-mapped |
| `BG-RES-MARA` | Mara private residential quarters | BASE | 1 | source-mapped |
| `BG-RES-RAVEN` | Raven private temporary room | NIGHT | 1 | source-mapped |
| `BG-RES-STEFFAN` | Steffan private hotel suite | NIGHT | 1 | source-mapped |
| `BG-SOC-BROADCAST` | Broadcast booth and control gallery | AFTERMATH, BASE, EVENING, NIGHT | 13 | source-mapped |
| `BG-SOC-CAFE` | Tournament quiet café / archive café | AFTERMATH, BASE, EVENING, NIGHT | 4 | source-mapped |
| `BG-SOC-DANCE` | Dance, performance and music venue | EVENING, NIGHT | 4 | source-mapped |
| `BG-SOC-FUND` | Fundraiser and social event salon | EVENING | 1 | source-mapped |
| `BG-SOC-GALA` | Anniversary gala interior | BASE, EVENING, NIGHT | 17 | source-mapped |
| `BG-SOC-GARDEN` | Central glazed observation garden | BASE, DAY, EVENING, NIGHT | 14 | source-mapped |
| `BG-SOC-POOL` | Rooftop pool and training terrace | DAY, NIGHT, SUNSET | 10 | source-mapped |
| `BG-SOC-PRESS` | Press hall and interview atrium | AFTERMATH, BASE, DAY, EVENING, NIGHT | 12 | source-mapped |
| `BG-SOC-RESTAURANT` | Observation-deck restaurant and dining room | BASE, EVENING, NIGHT | 5 | source-mapped |
| `BG-SOC-TRANSIT` | Transit platform, passage and public promenade | BASE, EVENING, NIGHT, SUNSET | 6 | source-mapped |
| `BG-SOC-VIEW` | Main public observation deck / gallery | BASE, DAY, EVENING, NIGHT | 15 | source-mapped |
| `BG-SOC-VIEW-PRIVATE` | Private observation suite and lounges | AFTERMATH, BASE, DAY, EVENING, NIGHT | 16 | source-mapped |
| `BG-TEC-EXPERIMENT` | Experimental equipment / demonstration wing | BASE, DAY, NIGHT | 9 | source-mapped |
| `BG-TEC-HANGAR` | Pilots’ HAR hangar and maintenance bay | AFTERMATH, BASE, EVENING, NIGHT | 13 | source-mapped |
| `BG-TEC-LIFE` | Coolant / coupling safety and life-support wing | BASE, DAY, EMERGENCY, NIGHT | 8 | source-mapped |
| `BG-TEC-OPERATIONS` | Research and maintenance operations center | AFTERMATH, BASE, EMERGENCY | 6 | source-mapped |
| `BG-TEC-SERVICE` | Back-of-house service corridors and technician desk | BASE, DAY, EMERGENCY, EVENING, NIGHT | 14 | source-mapped |

## Art prompting notes

Use the full prompt from `background_states.csv` and, after generating the first image, use it as a visual reference for all other states of that location. Keep geometry, window position, exterior Jupiter orientation, and perspective identical for those variants. Source sluglines are in the JSON registry for review.

## Scope and staging coverage

This is a **production candidate** based on 12 currently active pilot scripts plus the Christian subplot, not a claim that every background has been visually approved. A total of 122 scene headings lacked an explicit INT/EXT location (112 single-background staging proposals + 10 multi-background montage cuts). Their backgrounds are therefore script-editor staging proposals, even where a likely site is obvious. Scene-specific variants and montage references may require more than one rendered plate. Historical scene-card banks are indexed separately but are not newly declared active in the screenplay authority.

**v5.7 correction:** `scene_background_bindings.csv` was regenerated from scratch against the actual `CURRENT_RELEASE.md`-active script files. Every one of the 18 scripts it previously referenced was a stale, superseded revision (e.g. Lyra v0.5 instead of active v0.8, Crystal v0.7 instead of active v0.10, Raven v0.6 instead of active v0.9) -- line numbers and some scene-adjacent content no longer matched. The regenerated file was verified against `test_background_registry.py` (4/4 pass) and spot-checked line-by-line against the active files. Per-directory staging-provisional counts matched the old (stale) file exactly, which is why the headline "scenes without an explicit location" count didn't change -- what changed is that the line numbers and scene names now actually correspond to the current canon text. **`background_registry.json`'s `source_scenes`/`scene_count`/`inferred_uses` fields were NOT regenerated** -- they still reference the same old script versions and are a known, still-open staleness issue (tracked in `manifest.json`), separate from the now-corrected CSV.

**v5.8 ratification:** the author reviewed the corrected 122-scene list (112 `staging-provisional` + 10 `source-prose-montage`) and approved all of them as-is. `scene_background_bindings.csv` now carries an `author_ratified` column (`v5.8` for these 122 rows, blank for the 327 rows that already had an explicit slugline). This records *approval of the assigned background*, not a retroactive claim that the underlying prose now contains an explicit slugline -- the `binding` column's `staging-provisional`/`source-prose-montage` values, and the matching inline `[BG: ... | STAGING PROVISIONAL — no source slugline]` tags in the screenplay files themselves, are left as-is because they state a true fact about the source text (no INT/EXT line present), which ratifying the location choice doesn't change. No further script-editor review is required for these 122 scenes before image production.
