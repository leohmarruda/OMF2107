import sys
import unittest
from pathlib import Path
from dataclasses import replace
sys.path.insert(0, str(Path(__file__).resolve().parent))
from kreissack_arc_state import PILOTS, KreissackSceneState, available_scenes

class KreissackSceneTests(unittest.TestCase):
    def test_no_flashback_before_document(self):
        for day in range(0,30):
            s=KreissackSceneState(day=day)
            self.assertNotIn('K0_2092_FLASHBACK_POST_E5',available_scenes(s))

    def test_false_early_e5_rejected(self):
        for day in (0,10,12,13,29):
            with self.assertRaises(ValueError):
                available_scenes(KreissackSceneState(day=day,e5_authenticated=True))

    def test_2092_flashback_and_two_truths_are_after_proof(self):
        s=KreissackSceneState(day=30,e5_authenticated=True,
            relay_activation_started=True,boss_defeated=True,nova_destroyed=True)
        self.assertIn('K0_2092_FLASHBACK_POST_E5',available_scenes(s))
        self.assertIn('K7_TWO_TRUTHS_POSTSCRIPT',available_scenes(s))
        self.assertNotIn('K7_TWO_TRUTHS_POSTSCRIPT',available_scenes(replace(s,nova_destroyed=False)))

    def test_no_survival_documentary_before_act_three(self):
        with self.assertRaises(ValueError):
            available_scenes(KreissackSceneState(day=5,survival_discovered=True))
        s=KreissackSceneState(day=10,survival_discovered=True)
        self.assertIn('K1_ARCHIVAL_RECOVERY',available_scenes(s))
        self.assertNotIn('K2_RETROSPECTIVE_REPLAY',available_scenes(s))

    def test_rescue_is_day_twelve_and_not_full_revelation(self):
        self.assertIn('K3_RESCUE_REFLECTION',available_scenes(KreissackSceneState(day=12,rescue_verified=True)))
        self.assertNotIn('K3_RESCUE_REFLECTION',available_scenes(KreissackSceneState(day=13,rescue_verified=True)))
        with self.assertRaises(ValueError):
            available_scenes(KreissackSceneState(day=11,rescue_verified=True))

    def test_preactivation_carries_no_tournament_assumption(self):
        for pilot in PILOTS:
            self.assertIn('K4_PREACTIVATION_BARGAIN',available_scenes(
                KreissackSceneState(day=13,selected_pilot=pilot)))

    def test_failed_isolation_requires_started_relay(self):
        with self.assertRaises(ValueError):
            available_scenes(KreissackSceneState(day=13,attempted_isolation_failed=True))
        s=KreissackSceneState(day=13,relay_activation_started=True,attempted_isolation_failed=True)
        self.assertIn('K5_FAILED_COMMAND',available_scenes(s))
        self.assertNotIn('K5_FAILED_COMMAND',available_scenes(replace(s,composite_revealed=True)))

    def test_flashback_doesnt_require_ravens_testimony(self):
        for pilot in PILOTS:
            self.assertIn('K0_2092_FLASHBACK_POST_E5',available_scenes(
                KreissackSceneState(day=30,selected_pilot=pilot,e5_authenticated=True)))

    def test_default_sacrifice_requires_physical_conditions(self):
        s=KreissackSceneState(day=13,relay_activation_started=True,boss_defeated=True,
            gateway_damaged=True,bio_safety_path_intact=True,destruction_irreversible=True,
            core_ejection_pending=True)
        self.assertIn('K6_HARDWIRED_LAST_CHOICE',available_scenes(s))
        for field in ('gateway_damaged','bio_safety_path_intact',
                      'destruction_irreversible','core_ejection_pending','boss_defeated'):
            self.assertNotIn('K6_HARDWIRED_LAST_CHOICE',available_scenes(replace(s,**{field:False})))
        self.assertNotIn('K6_HARDWIRED_LAST_CHOICE',available_scenes(replace(s,complete_backup_exists=True)))

    def test_defeat_does_not_require_official_championship(self):
        for pilot in PILOTS:
            s=KreissackSceneState(day=13,selected_pilot=pilot,
                relay_activation_started=True,boss_defeated=True,
                gateway_damaged=True,destruction_irreversible=True,core_ejection_pending=True)
            self.assertIn('K6_HARDWIRED_LAST_CHOICE',available_scenes(s))

    def test_rejected_early_composite_reveal(self):
        for day in (0,10,12):
            with self.assertRaises(ValueError):
                available_scenes(KreissackSceneState(day=day,composite_revealed=True))

    def test_integrated_script_contains_shared_insertions_once(self):
        root=Path(__file__).resolve().parents[1]
        active=(root/'04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.4.md').read_text()
        self.assertEqual(active.count('## SCENE 4K —'),1)
        self.assertEqual(active.count('## SCENE 6K —'),1)
        self.assertLess(active.index('## SCENE 4K —'),active.index('# SCENE 5 —'))
        self.assertLess(active.index('## SCENE 6K —'),active.index('# SCENE 7 —'))
        self.assertIn('CORE RETENTION INTERLOCK — HARDWIRED',active)
        self.assertIn('Apparently, I can still surprise you.',active)

    def test_older_script_and_original_lore_are_retained(self):
        root=Path(__file__).resolve().parents[1]
        self.assertTrue((root/'04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.3.md').exists())
        self.assertTrue((root/'01_Original_Sources/OMF2097_LORE.md').exists())
        self.assertTrue((root/'02_Story_Bibles/Master_Story_Bible_v2.3.md').exists())

if __name__=='__main__': unittest.main()
