import csv,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R/'07_Tournament_Model'))
class V52ReleaseGate(unittest.TestCase):
 def test_current_policy_snapshot_literal_facts(self):
  """Weak sanity check only: these phrases literally occur somewhere in
  CURRENT_RELEASE.md. This guards against accidental deletion of a line; it
  does NOT verify the policy is actually true or implemented -- see
  test_current_policy_matches_implementation for the facts that are
  cross-checkable against real code/data, and v5.2's own self-audit for why
  this distinction matters (manifest.json/FINAL_STABILIZATION_AUDIT_v5.2.md
  previously over-trusted doc-only claims like this one)."""
  t=(R/'00_README/CURRENT_RELEASE.md').read_text()
  for val in ('v5.8 background locations ratified','NPC-vs-NPC fights occur **offscreen**','Cossette–Ibrahim'):
   self.assertIn(val,t)
 def test_current_policy_matches_implementation(self):
  """Real cross-check for the two policy claims in the snapshot that are
  actually backed by live code/data, instead of trusting the changelog
  prose by itself:
  - '51 provisional' NPC outcomes: cross-checked against
    npc_outcome_registry.provisional_preview_status(), the same live
    count 07_Tournament_Model/test_provisional_npc_v46.py independently
    verifies against the ledger CSV.
  - 'persisted uniform random permutation' three-way tiebreak: cross-checked
    against tournament_validator.py actually containing the
    'recorded_uniform_random_draw' ranking method the policy describes."""
  from npc_outcome_registry import provisional_preview_status
  status = provisional_preview_status()
  t=(R/'00_README/CURRENT_RELEASE.md').read_text()
  self.assertIn(f"{status['provisionally_approved']} provisional", t)
  self.assertEqual(status['provisionally_approved'], 51)
  validator_src = (R/'07_Tournament_Model/tournament_validator.py').read_text()
  self.assertIn('recorded_uniform_random_draw', validator_src)
  self.assertIn('persisted uniform random permutation', t)
 def test_scene_inventory_source_lines(self):
  with (R/'31_Cross_POV_Integration/ACTIVE_SCENE_INVENTORY_v3.3.csv').open(newline='') as f: rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),405)
  for row in rows:
   s=(R/row['source']).read_text().splitlines()[int(row['line'])-1]
   self.assertIn(row['scene_id'].lower().replace(' ',''),s.lower().replace(' ',''))
if __name__=='__main__':unittest.main()
