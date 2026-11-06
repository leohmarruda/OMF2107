import csv, unittest
from pathlib import Path
from npc_provisional_v46 import PROVISIONAL_NPC_WINNERS, effective_preview_winners
from npc_author_approved_v45 import AUTHOR_APPROVED_NPC_WINNERS
from npc_outcome_registry import provisional_preview_status, current_author_approval_status, require_complete_npc_table
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS
class ProvisionalNPCV46Tests(unittest.TestCase):
    def test_counts_and_distinct_authority(self):
        s=provisional_preview_status()
        self.assertEqual((s['cinematic_canon'],s['explicit_author_approved'],s['provisionally_approved']),(7,8,51))
        self.assertEqual(len(s['winners']),66)
        self.assertFalse(s['final_canon_signed_off'])
        self.assertEqual(len(current_author_approval_status()['pending_pairs']),51)
    def test_author_override_mara_steffan(self):
        pair=frozenset(('Mara','Steffan'))
        self.assertEqual(effective_preview_winners()[pair],'Steffan')
    def test_final_gate_not_implicitly_weakened(self):
        with self.assertRaises(ValueError): require_complete_npc_table(AUTHOR_APPROVED_NPC_WINNERS)
    def test_preview_complete_and_canon_immutable(self):
        self.assertEqual(require_complete_npc_table({**PROVISIONAL_NPC_WINNERS,**AUTHOR_APPROVED_NPC_WINNERS}),effective_preview_winners())
        for pair,winner in DEFAULT_KNOCKOUT_WINNERS.items(): self.assertEqual(effective_preview_winners()[pair],winner)
    def test_ledger_provenance(self):
        rows=list(csv.DictReader(Path(__file__).with_name('NPC_OUTCOME_APPROVAL_LEDGER_v4.6.csv').open(encoding='utf-8',newline='')))
        self.assertEqual(len(rows),66)
        self.assertEqual(sum(r['status']=='PROVISIONALLY_APPROVED_v4.6' for r in rows),51)
        for r in rows:
            p=frozenset((r['fighter_a'],r['fighter_b']))
            if p in PROVISIONAL_NPC_WINNERS: self.assertEqual(r['approval_decision'],PROVISIONAL_NPC_WINNERS[p])
if __name__=='__main__': unittest.main()
