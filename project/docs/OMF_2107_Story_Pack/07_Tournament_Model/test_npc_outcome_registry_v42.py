import unittest
from npc_outcome_registry import audit_approved_overrides, require_complete_npc_table
from npc_pair_reachability import reachability
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS

class OutcomeRegistryTests(unittest.TestCase):
    def test_defaults_leave_59_pending(self):
        status = audit_approved_overrides({})
        self.assertEqual(status['resolved_pairs'],7)
        self.assertEqual(len(status['pending_pairs']),59)
        self.assertFalse(status['ready_for_production'])
    def test_complete_explicit_table_passes(self):
        outstanding = reachability().keys() - DEFAULT_KNOCKOUT_WINNERS.keys()
        overrides = {p:sorted(p)[0] for p in outstanding}
        table = require_complete_npc_table(overrides)
        self.assertEqual(len(table),66)
    def test_cannot_override_canon(self):
        pair, winner = next(iter(DEFAULT_KNOCKOUT_WINNERS.items()))
        other = next(x for x in pair if x != winner)
        with self.assertRaisesRegex(ValueError,'Cannot override'):
            audit_approved_overrides({pair:other})
    def test_rejects_incomplete_and_invalid(self):
        with self.assertRaisesRegex(ValueError,'59 reachable'):
            require_complete_npc_table({})
        with self.assertRaisesRegex(ValueError,'Invalid approved'):
            audit_approved_overrides({frozenset(('Ari','NotAFighter')):'Ari'})

if __name__ == '__main__':unittest.main()
