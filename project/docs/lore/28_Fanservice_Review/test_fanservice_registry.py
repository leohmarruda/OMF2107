import csv, re, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def _active_screenplay_table():
    """Parse the one authoritative '<pilot> -> current active screenplay file(s)'
    mapping out of 00_README/CURRENT_RELEASE.md's
    '## Current active screenplay and route specifications' table, plus the
    one Christian_Subplot line that lives outside that table. Multi-file
    entries (Ari's six chapters) are split on '+'."""
    text = (ROOT / '00_README/CURRENT_RELEASE.md').read_text(encoding='utf8')
    table = {}
    for line in text.splitlines():
        m = re.match(r'\|\s*([\w-]+)\s*\|\s*`([^`]+)`\s*\|', line)
        if m and m.group(1) not in ('Pilot',):
            files = [f.strip() for f in m.group(2).split('+')]
            # Multi-file entries (Ari's six chapters) only state the
            # directory once, on the first filename -- carry it forward.
            if files and '/' in files[0]:
                directory = files[0].rsplit('/', 1)[0]
                files = [f if '/' in f else f'{directory}/{f}' for f in files]
            table[m.group(1)] = files
    m = re.search(r'Supporting subplot — Christian:\*{0,2}\s*`([^`]+)`', text)
    if m:
        table['Christian'] = [m.group(1)]
    return table

_ANNOTATION_LINE = re.compile(r'(?m)^\*\*\[(FANSERVICE|GESTURE):.*?\]\*\*\n?')

def _strip_annotation_lines(text: str) -> str:
    """Drop whole-line [FANSERVICE: ...] / [GESTURE: ...] tags. Both are
    additive editorial annotations layered on in later release passes
    (Fanservice v2.9, Gesture Registry v3.1) and are expected to differ
    between a tagged scene's recorded source version and today's active
    version even when the underlying dialogue/action text is unchanged."""
    return _ANNOTATION_LINE.sub('', text)

def _tagged_block(fs_id: str, text: str) -> str:
    """Return the scene heading + the fanservice-tagged body that follows a
    given '[FANSERVICE: <fs_id> | ...]' tag, up to (not including) the next
    heading line, or end of file."""
    lines = text.splitlines()
    tag_i = next(i for i, l in enumerate(lines) if f'[FANSERVICE: {fs_id} |' in l)
    heading_i = tag_i
    while heading_i > 0 and not lines[heading_i].lstrip().startswith('#'):
        heading_i -= 1
    end_i = next((j for j in range(tag_i + 1, len(lines))
                  if lines[j].lstrip().startswith('#')), len(lines))
    return '\n'.join(lines[heading_i:end_i])

class FanserviceRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with (ROOT/'28_Fanservice_Review/Fanservice_Review_Index_v1.0.csv').open(newline='', encoding='utf8') as file:
            cls.rows=list(csv.DictReader(file))
    def test_unique_ids(self):
        self.assertEqual(len(set(r['id'] for r in self.rows)),len(self.rows))
    def test_all_recorded_tags_are_present_in_source(self):
        for r in self.rows:
            txt=(ROOT/r['source']).read_text(encoding='utf8')
            self.assertEqual(txt.count('[FANSERVICE: '+r['id']+' |'),1,r['id'])
    def test_tags_reversible_for_active_scripts(self):
        for r in self.rows:
            if r['status']!='ACTIVE_SCRIPT_REVIEW':continue
            original=(ROOT/r['source_previous']).read_text(encoding='utf8')
            updated=(ROOT/r['source']).read_text(encoding='utf8')
            updated=updated.split('\n',1)[1] # editorial header
            # Strip both FANSERVICE and GESTURE annotation lines: a
            # source/source_previous pair that straddles the v3.1 Gesture
            # Registry pass (which added GESTURE lines pack-wide, same as
            # this pass added FANSERVICE lines) is still reversible once
            # both additive annotation layers are removed.
            updated=_strip_annotation_lines(updated)
            self.assertEqual(updated,original,r['source'])
    def test_sources_cited_in_changelog(self):
        """Weak sanity check only: the recorded source filename is mentioned
        *somewhere* in CURRENT_RELEASE.md (current OR historical sections).
        This does NOT verify the source is the currently-active script for
        that pilot -- see test_tagged_content_matches_current_active_script
        for that. (Renamed from test_sources_in_index_point_to_new_versions,
        which asserted currency but only ever checked this weaker fact.)"""
        curr=(ROOT/'00_README/CURRENT_RELEASE.md').read_text(encoding='utf-8')
        for r in self.rows:
            if r['status']=='ACTIVE_SCRIPT_REVIEW':self.assertIn(Path(r['source']).name,curr)
    # Known, investigated exceptions -- do NOT add to this silently. Each
    # entry here means: a human (or a prior review pass) has confirmed the
    # tagged scene's cached text genuinely diverged from the live active
    # script for a *substantive, intentional* reason, and the Fanservice
    # index has not yet been re-snapshotted to match. This lets the test
    # below stay a real tripwire for *undocumented* drift (it still fails
    # loudly for anything not listed here) while not re-raising a drift
    # that's already been triaged.
    #   FS-CRYSTAL-C3-2 and FS-RAVEN-R3-2: v4.7 relationship-canon
    #   clarification (00_README/CURRENT_RELEASE.md, "New direct-author
    #   authority" / Relationship_Canon_Clarifications_v4.7.md) rewrote
    #   both halves of this mirrored Crystal/Raven exploit scene -- Crystal
    #   no longer recognizes Raven's manipulation in the moment on either
    #   side (she did in the v0.8/v0.9 -> v0.9/v0.8 text this index still
    #   cites). That is an approved, documented canon change, not a bug,
    #   but it means both Fanservice entries' cached synopses of "what the
    #   EXPLOIT/predatory branch does" are now narratively wrong until
    #   someone re-snapshots them against the current v0.9 (Crystal v0.10)
    #   text. Flagged for the author; not silently corrected here.
    KNOWN_STALE_TAGGED_CONTENT = {'FS-CRYSTAL-C3-2', 'FS-RAVEN-R3-2'}

    def test_tagged_content_matches_current_active_script(self):
        """Real currency check. The Fanservice index's 'source' column is
        allowed to be one or more versions behind CURRENT_RELEASE.md's
        authoritative active screenplay for that pilot/subplot (campaign
        drafts move faster than the index is regenerated) -- but if it is
        behind, the exact tagged scene text it recorded must still appear
        verbatim in the file that is *actually* active today. If a later
        screenplay revision silently rewrote words inside a tagged span,
        this fails; the old weak test could not have caught that."""
        active = _active_screenplay_table()
        unexplained_drift = []
        for r in self.rows:
            if r['status'] != 'ACTIVE_SCRIPT_REVIEW':
                continue
            pilot = r['campaign']
            active_files = active.get(pilot)
            self.assertIsNotNone(active_files, f"no active-screenplay entry for {pilot!r} ({r['id']})")
            if r['source'] in active_files:
                continue  # index already points at the live active file
            source_text = (ROOT / r['source']).read_text(encoding='utf8')
            block = _strip_annotation_lines(_tagged_block(r['id'], source_text))
            matched_somewhere = False
            for active_path in active_files:
                active_text = _strip_annotation_lines((ROOT / active_path).read_text(encoding='utf8'))
                if block in active_text:
                    matched_somewhere = True
                    break
            if not matched_somewhere and r['id'] not in self.KNOWN_STALE_TAGGED_CONTENT:
                unexplained_drift.append(
                    f"{r['id']}: tagged scene recorded against {r['source']} no longer "
                    f"matches verbatim in the current active file(s) {active_files} for {pilot!r}"
                )
        self.assertEqual(unexplained_drift, [], '\n' + '\n'.join(unexplained_drift))
if __name__=='__main__':unittest.main()
