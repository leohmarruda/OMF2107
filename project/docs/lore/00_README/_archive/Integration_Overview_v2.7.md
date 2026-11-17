# OMF 2107 — Integration Overview v2.7: Shared Background Registry

**Based on:** Story Pack v2.6. **Scope:** background art coding only; canonical event timeline, pilot outcomes, romance flags, and character dialogue unchanged.

- **59** reusable base environments (including historical montage plates).
- **160** concrete `BG-CODE@STATE` variants for image production.
- **449** per-script background binding records covering 18 active screenplay source files: Ari's six chapters, the other 11 pilots, and Christian's subplot.
- **336** direct, unambiguous single or alternate scene-location bindings; **112** editorial/provisional staging assignments where the script lacks a location slugline; **1** archival montage sourced from narrative prose. (A compound slugline can map to multiple plates.)
- All old manuscript versions preserved. New active variants are listed in `00_README/CURRENT_RELEASE.md` and the registry's `SCRIPT_REVISION_MAP.md`.

**Catalog:** `26_Background_Registry/BACKGROUND_CATALOG.md`. Use `background_registry.json`, `background_registry.csv` and `background_states.csv` for assets; `scene_background_bindings.csv` for injection, review and traceability. The format `[BG: BG-ARE-MAIN@DAY]` is a screenplay annotation, not an automatic renderer API. The implementation team should load the CSV/JSON and translate it to the game's scene runtime.

**Caveats:** This step does not resolve the game's provisional tournament tie-break, NPC match results, or a global relationship save state. Optional historical scene-card banks have a separate limited source-location index, not active scene-authority rewrites. Provisional stage assignments should be reviewed before commissioning artwork.
