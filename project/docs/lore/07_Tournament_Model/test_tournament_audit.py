import unittest
from tournament_validator import simulate, CYCLE_SEED
from tournament_audit import enumerate_routes, summarize

class TournamentAuditTests(unittest.TestCase):
    def test_all_input_tuples_retain_provenance(self):
        rows = enumerate_routes()
        summary = summarize(rows)
        self.assertEqual(summary['total_input_tuples'], 384)
        self.assertLessEqual(summary['canonical_input_paths_after_ignored_bits'], 384)
        self.assertTrue(all(r['champion'] for r in rows))
        self.assertTrue(all(r['canon_ready'] == (not r['unapproved_cycle_groups'] and not r['provisional_npc_match_ids']) for r in rows))

    def test_circular_seed_cannot_pass_strict_mode_implicitly(self):
        with self.assertRaisesRegex(ValueError, 'Unapproved circular'):
            simulate('Ari', (True, False), (False,), require_authored=True)

    def test_default_bracket_is_authored_and_alternate_needs_authoring(self):
        result = simulate('Ari', (False, True), (True, True, True), require_authored=True)
        self.assertTrue(result['audit']['canon_ready'])
        with self.assertRaisesRegex(ValueError, 'Missing authored NPC result'):
            simulate('Ari', (True, True), (True, True, True), require_authored=True)

    def test_bad_npc_override_winner_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Invalid NPC'):
            simulate('Ari', (False, True), (True, True, True), npc_knockout_winners={frozenset(('Crystal', 'Ren')): 'Ari'})

    def test_bad_seed_rejected_even_when_not_used(self):
        seeds = dict(CYCLE_SEED)
        seeds['A'] = ('Crystal', 'Crystal', 'Selene')
        with self.assertRaisesRegex(ValueError, 'Invalid cycle seed'):
            simulate('Ari', (False, True), (True, True, True), cycle_seed=seeds)

    def test_player_path_has_no_npc_override_for_player_match(self):
        result = simulate('Ari', (False, True), (True, True, True), npc_knockout_winners={frozenset(('Ari', 'Mara')): 'Mara'})
        self.assertEqual(result['champion'], 'Ari')

if __name__ == '__main__':
    unittest.main()
