import unittest
from tournament_validator import simulate
from offscreen_npc_results import project_board


class OffscreenNpcResultTests(unittest.TestCase):
    def test_offscreen_fights_never_render(self):
        route = simulate('Ari', (False, True), (True, True, True))
        board = project_board(route, allow_draft=True)
        self.assertEqual(len(board['bracket']), 19)
        self.assertTrue(board['npc_results'])
        self.assertTrue(all(not m['render_fight'] for m in board['npc_results']))
        self.assertTrue(all(m['display_kind'] == 'npc_offscreen_result' for m in board['npc_results']))

    def test_unscored_results_not_fabricated(self):
        route = simulate('Ari', (False, True), (True, True, True))
        board = project_board(route, allow_draft=True)
        self.assertTrue(all(m['scores'] is None for m in board['bracket']))
        self.assertTrue(all(not m['score_available'] for m in board['bracket']))

    def test_reject_draft_in_production(self):
        route = simulate('Ari', (False, True), (False,))
        self.assertFalse(route['audit']['canon_ready'])
        with self.assertRaisesRegex(ValueError, 'draft-only'):
            project_board(route)

    def test_proposed_winners_explicitly_tagged(self):
        candidate = None
        # Find a branch whose NPC knockouts use a review-pending pair.
        import itertools
        for name in ('Ari', 'Mara', 'Crystal', 'Lyra', 'Ren'):
            for gw in itertools.product((False, True), repeat=2):
                for kw in itertools.product((False, True), repeat=3):
                    route = simulate(name, gw, kw, use_proposed_npc=True)
                    if route['audit']['proposed_npc_match_ids']:
                        candidate = route
                        break
                if candidate: break
            if candidate: break
        self.assertIsNotNone(candidate)
        board = project_board(candidate, allow_draft=True)
        self.assertTrue(board['is_draft'])
        self.assertEqual(set(board['requires_author_approval']), set(candidate['audit']['proposed_npc_match_ids']))

    def test_scored_group_results_projected_without_modification(self):
        route = simulate('Ari', (False, True), (False,), group_match_scores={'GA1':(10,9)})
        board = project_board(route, allow_draft=True)
        self.assertEqual(board['bracket'][0]['scores'], {'Crystal':10,'Ari':9})
        self.assertFalse(board['bracket'][1]['score_available'])

if __name__ == '__main__': unittest.main()
