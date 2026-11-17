import itertools
import unittest
from ari_route_validator import simulate_ari_screen


class AriRouteTests(unittest.TestCase):
    def test_four_standings(self):
        outcomes = {
            (True, False): ("GA_DEFAULT", 2, "Mara"),
            (True, True): ("GA_ARI_WINNER", 1, "Ren"),
            (False, True): ("GA_CYCLE", 2, "Mara"),
            (False, False): ("GA_OUT", 3, None),
        }
        for flags, expected in outcomes.items():
            with self.subTest(flags=flags):
                r=simulate_ari_screen(*flags, (True, True, True))
                self.assertEqual((r["group_case"],r["ari_group_rank"],r["qf_opponent"]),expected)

    def test_all_thirty_two_inputs(self):
        for bits in itertools.product((False, True), repeat=5):
            with self.subTest(bits=bits):
                r=simulate_ari_screen(bits[0], bits[1], bits[2:])
                self.assertEqual(r["ari_receives_trophy"],r["champion"]=="Ari")
                self.assertEqual(r["ari_finalist"],"Ari" in r["finalists"])
                if not r["qualified"]:
                    self.assertIsNone(r["qf_id"])
                    self.assertIn("A4_GROUP_OUT_ARCHIVE_INVESTIGATION",r["scene_keys"])
                    self.assertNotIn("A7_ARI_TROPHY",r["scene_keys"])
                if not r["ari_finalist"]:
                    self.assertNotIn("A7_ARI_FINAL_WIN",r["scene_keys"])
                self.assertEqual([x["key"] for x in r["events"][-5:]],
                                 ["COOLANT_RESCUE", "S_CD", "FINAL", "SPECIAL_NOVA", "EPILOGUE"])
                self.assertEqual(r["events"][-2]["official_match"],False)
                self.assertTrue(all(x["winner"] in (x["left"],x["right"])
                                    and x["loser"] != x["winner"]
                                    for x in r["tournament"]["matches"]))

    def test_final_win_and_loss_distinct(self):
        victory=simulate_ari_screen(True,False,(True,True,True))
        defeat=simulate_ari_screen(True,False,(True,True,False))
        self.assertEqual(victory["champion"],"Ari")
        self.assertEqual(defeat["champion"],"Lyra")
        self.assertIn("A7_ARI_TROPHY",victory["scene_keys"])
        self.assertNotIn("A7_ARI_TROPHY",defeat["scene_keys"])
        self.assertIn("A7_OTHER_TROPHY",defeat["scene_keys"])

    def test_group_exit_no_phantom_quarterfinal(self):
        r=simulate_ari_screen(False,False,(True,True,True))
        self.assertEqual(r["player_elimination_match"],"GROUP_STAGE")
        q2=next(m for m in r["tournament"]["matches"] if m["id"]=="Q2")
        self.assertEqual(set((q2["left"],q2["right"])),{"Selene","Mara"})
        self.assertNotIn("Ari",r["finalists"])

    def test_fight_results_independent_of_romance_neuro_and_evidence(self):
        a=simulate_ari_screen(True,True,(True,True,True))
        b=simulate_ari_screen(True,True,(True,True,True),romance="mara_romance",
            mara_reciprocal=True,neural_program="extended",evidence_approach="witness_privacy")
        self.assertEqual(a["tournament"]["matches"],b["tournament"]["matches"])

    def test_leena_requires_independent_reciprocity_and_recusal(self):
        for reciprocal,recused in [(False,False),(True,False),(False,True)]:
            with self.assertRaises(ValueError):
                simulate_ari_screen(True,False,(True,True,True),romance="leena_romance",
                                    leena_reciprocal=reciprocal,leena_recused=recused)
        r=simulate_ari_screen(True,False,(True,True,True),romance="leena_romance",
                              leena_reciprocal=True,leena_recused=True)
        self.assertEqual(r["romance"],"leena_romance")

    def test_mara_romance_requires_consent(self):
        with self.assertRaises(ValueError):
            simulate_ari_screen(True,False,(True,True,True),romance="mara_romance")

    def test_nondefault_other_finalist(self):
        overrides={frozenset(("Angel","Lyra")):"Angel",
                   frozenset(("Steffan","Angel")):"Angel"}
        r=simulate_ari_screen(True,False,(True,True,True),npc_knockout_winners=overrides)
        self.assertEqual(set(r["finalists"]),{"Ari","Angel"})
        self.assertEqual(r["champion"],"Ari")

    def test_provisional_npc_not_canon(self):
        r=simulate_ari_screen(False,False,())
        self.assertTrue(r["provisional_npc_match_ids"])
        self.assertFalse(r["npc_results_ready_for_canon"])
        self.assertTrue(r["uses_npc_test_fallback"])

    def test_invalid_choices(self):
        with self.assertRaises(ValueError): simulate_ari_screen(1,True,())
        with self.assertRaises(ValueError): simulate_ari_screen(True,False,(),neural_program="forced")


if __name__ == "__main__":
    unittest.main()
