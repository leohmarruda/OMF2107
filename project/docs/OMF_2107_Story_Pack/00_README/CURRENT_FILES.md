# Current files: which version is live

One table for "which file do I use?". Source of truth for the release is `CURRENT_RELEASE.md` (v5.8); this file lists the live file for each document family and where the superseded versions are. Superseded versions are kept for provenance in an `_archive/` folder next to the live file. A few superseded files stay in place because tests, registries or the release manifest name them by path.

Rule: where a family has several versions, the highest version is current. Exceptions are noted below.

## Ari (`04_Screenplay_Reconstructions/`, route spec in `14_Ari_Campaign/`)

| Document | Current |
|---|---|
| Chapter 1 Anniversary | `Chapter_01_Anniversary_v0.6.md` |
| Chapter 2 Champions' Shadow | `Chapter_02_Champions_Shadow_v0.7.md` |
| Chapter 3 Trouble With Attraction | `Chapter_03_Trouble_With_Attraction_v0.7.md` |
| Chapter 4 No Holding Back | `Chapter_04_No_Holding_Back_v0.7.md` |
| Chapter 5 Fractures | `Chapter_05_Fractures_v0.7.md` |
| Chapter 6 One Must Fall | `Chapter_06_One_Must_Fall_v0.8.md` |
| Route spec | `14_Ari_Campaign/Ari_Route_Spec_v0.1.md` |
| Scene cards (proposal only) | `Spicy_and_Fanservice_Scene_Cards_v0.2.md`, `Optional_Relationship_Scene_Cards_v0.1.md` |

The game script `project/data/story/ari.story` is written against these versions.

## Pilot campaigns

| Pilot | Screenplay | Route spec |
|---|---|---|
| Lyra (09) | v0.8 | `Lyra_Route_Spec_v0.1` |
| Mara (10) | v0.6 | `Mara_Route_Spec_v0.1` |
| Ren (11) | v0.6 | `Ren_Route_Spec_v0.1` |
| Angel (12) | v0.6 | `Angel_Route_Spec_v0.1` |
| Crystal (15) | v0.10 | v0.3 |
| Raven (16) | v0.9 | v0.2 |
| Christian (18) | storyline v0.6 | route and evidence spec v0.2 |
| Jean-Paul (20) | v0.5 | `Jean_Paul_Route_Spec_v0.1` |
| Steffan (21) | v0.7 | v0.2 |
| Dante (22) | v0.7 | v0.2 |
| Selene (23) | v0.5 | `Selene_Route_Spec_v0.1` |
| Milano (24) | v0.5 | `Milano_Route_Spec_v0.1` |

## Canon and overviews

| Document | Current | Note |
|---|---|---|
| Master Story Bible | `Master_Story_Bible_v2.7.md` | |
| Devroe Shuttle Case Canon | `Devroe_Shuttle_Case_Canon_v1.7.md` | higher version chosen over v1.5 |
| Steffan Character Addendum | `Steffan_Character_Addendum_v2.3.md` | higher version chosen over v2.1 |
| Dante Character Addendum | `Dante_Character_Addendum_v2.3.md` | |
| Raven Canon Addendum | `Raven_Canon_Addendum_v1.4.md` | `Crystal_Raven_Canon_Addendum_v1.3.md` stays valid for Crystal's attraction and consent |
| Relationship Canon Clarifications | v4.8 and v4.7 together | v4.8 for Cossette, Ibrahim and Milano; v4.7 for Dante, Lyra, Crystal and Raven |
| Integration Overview | `Integration_Overview_v2.9.md` | later changes are in `CURRENT_RELEASE.md` |
| Devroe Scene Packet | `17_Devroe_Case/Devroe_Scene_Packet_v1.7.md` | |

## Still in their folders (not archived)

Older versions that tests, registries or `manifest.json` name by path were not moved, so the paths keep working. Examples: the Ari chapter versions listed in `background_registry.json`, the scene cue CSVs and the route validators, and `Dante_Character_Addendum_v2.2.md`. They are superseded all the same.

## Other registries

`07_Tournament_Model`, `08_Relationship_Model`, `13_Cross_Campaign_Audit`, `19_Kreissack_Arc` and `25` to `33` keep their own version series and were not touched. `CURRENT_RELEASE.md` names the live file in each.
