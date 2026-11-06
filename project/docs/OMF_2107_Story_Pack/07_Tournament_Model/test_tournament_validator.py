"""Run: python3 -m unittest discover -s 07_Tournament_Model -p 'test_*.py' -v"""
import itertools
import unittest
from tournament_validator import GROUPS, NPC_KNOCKOUT_PRIORITY, simulate

class TestTournament(unittest.TestCase):
    def test_default_ari(self):
        result = simulate("Ari", (False, True), (True, True, True))
        self.assertEqual(result["champion"], "Ari")
        self.assertEqual(result["player_match_ids"],
                         ["GA1", "GA3", "Q2", "S_AB", "FINAL"])
        self.assertEqual([m["winner"] for m in result["matches"] if m["id"] in ("Q1", "Q2", "Q3", "Q4", "S_AB", "S_CD", "FINAL")],
                         ["Crystal", "Ari", "Steffan", "Lyra", "Ari", "Lyra", "Ari"])

    def test_ari_beats_crystal_and_faces_ren(self):
        result = simulate("Ari", (True, True), (True, True, True))
        q1 = next(m for m in result["matches"] if m["id"] == "Q1")
        self.assertEqual({q1["left"], q1["right"]}, {"Ari", "Ren"})

    def test_ari_loses_qf_cannot_be_champion(self):
        result = simulate("Ari", (False, True), (False,))
        self.assertNotEqual(result["champion"], "Ari")
        self.assertEqual(result["player_elimination_match"], "Q2")

    def test_circular_group_results_are_not_drawn_fights(self):
        # A: Crystal>Selene, Selene>Ari, Ari>Crystal -> 1-1-1.
        result = simulate("Ari", (True, False), (False,))
        self.assertTrue(result["group_standings"]["A"]["circular_1_1_1"])
        self.assertEqual(result["group_standings"]["A"]["ranked"],
                         ["Crystal", "Ari", "Selene"])
        self.assertTrue(all(m["winner"] != m["loser"] for m in result["matches"]))

    def test_all_12_player_choices_and_outcomes(self):
        runs = 0
        for pilot in NPC_KNOCKOUT_PRIORITY:
            for bits in itertools.product((False, True), repeat=5):
                result = simulate(pilot, bits[:2], bits[2:])
                self.assertEqual(len(result["matches"]), 19)
                self.assertIn(result["champion"], NPC_KNOCKOUT_PRIORITY)
                self.assertEqual(result["used_group_results"], 2)
                runs += 1
        self.assertEqual(runs, 384)

    def test_all_pilots_can_win_championship(self):
        for pilot in NPC_KNOCKOUT_PRIORITY:
            result = simulate(pilot, (True, True), (True, True, True))
            self.assertEqual(result["champion"], pilot)

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            simulate("Ari", (True, ), (True, True, True))
        with self.assertRaises(ValueError):
            simulate("Ari", (True, None), (True, True, True))
        with self.assertRaises(ValueError):
            simulate("Ari", (True, True), ())

if __name__ == "__main__":
    unittest.main()
