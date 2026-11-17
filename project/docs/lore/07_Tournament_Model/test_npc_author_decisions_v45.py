import csv
import unittest
from pathlib import Path
from npc_author_approved_v45 import AUTHOR_APPROVED_NPC_WINNERS
from npc_outcome_registry import current_author_approval_status, approved_author_outcomes, require_complete_npc_table
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS

class AuthorNPCDecisionTests(unittest.TestCase):
    def test_eight_approved_decisions_exact(self):
        expected={
            frozenset(('Angel','Milano')):'Milano',
            frozenset(('Angel','Ren')):'Ren',
            frozenset(('Crystal','Lyra')):'Crystal',
            frozenset(('Dante','Ren')):'Dante',
            frozenset(('Jean-Paul','Selene')):'Jean-Paul',
            frozenset(('Mara','Selene')):'Selene',
            frozenset(('Mara','Steffan')):'Steffan',
            frozenset(('Raven','Steffan')):'Raven',
        }
        self.assertEqual(AUTHOR_APPROVED_NPC_WINNERS,expected)
        self.assertEqual(approved_author_outcomes(),expected)
    def test_existing_cinematic_results_unchanged(self):
        self.assertEqual(len(DEFAULT_KNOCKOUT_WINNERS),7)
        self.assertFalse(set(DEFAULT_KNOCKOUT_WINNERS)&set(AUTHOR_APPROVED_NPC_WINNERS))
    def test_51_pending_still_block_production(self):
        status=current_author_approval_status()
        self.assertEqual(status['resolved_pairs'],15)
        self.assertEqual(len(status['pending_pairs']),51)
        self.assertFalse(status['ready_for_production'])
        with self.assertRaisesRegex(ValueError,'51 reachable'):
            require_complete_npc_table(approved_author_outcomes())
    def test_ledger_matches_author_approval_registry(self):
        p=Path(__file__).with_name('NPC_OUTCOME_APPROVAL_LEDGER_v4.5.csv')
        rows=list(csv.DictReader(p.open(encoding='utf-8',newline='')))
        self.assertEqual(len(rows),66)
        self.assertEqual(sum(r['status']=='AUTHOR_APPROVED_v4.5' for r in rows),8)
        self.assertEqual(sum(r['status']=='PENDING_AUTHOR_APPROVAL' for r in rows),51)
        self.assertEqual(sum(bool(r['established_winner']) for r in rows),7)
        for r in rows:
            pair=frozenset((r['fighter_a'],r['fighter_b']))
            if pair in AUTHOR_APPROVED_NPC_WINNERS:
                self.assertEqual(r['approval_decision'],AUTHOR_APPROVED_NPC_WINNERS[pair])
                self.assertEqual(r['approved_by'],'Author')
            elif pair not in DEFAULT_KNOCKOUT_WINNERS:
                self.assertEqual(r['approval_decision'],'')
            else:
                self.assertEqual(r['established_winner'],DEFAULT_KNOCKOUT_WINNERS[pair])

if __name__=='__main__': unittest.main()
