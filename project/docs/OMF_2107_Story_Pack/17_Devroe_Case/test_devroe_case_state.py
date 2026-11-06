import itertools
import sys
from pathlib import Path
import unittest
from dataclasses import replace
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '16_Raven_Campaign'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '15_Crystal_Campaign'))
from devroe_case_state import HISTORICAL_FACTS, INDEPENDENT_EVIDENCE, case_for_route
from raven_route_validator import RavenChoices, simulate_raven_screen
from crystal_route_validator import CrystalChoices, simulate_crystal_screen

class DevroeCaseTests(unittest.TestCase):
    def test_fixed_truth_and_independent_evidence_across_raven_choices(self):
        for stmt, pressure, hearing in itertools.product(
            ('full','selective','false_denial'),('leave','exploit'),('testify','obstruct')):
            r=simulate_raven_screen(False,False,choices=RavenChoices(
                shuttle_statement=stmt,crystal_pressure=pressure,hearing_response=hearing))
            self.assertEqual(r['devroe_case'].historical_facts,HISTORICAL_FACTS)
            self.assertEqual(r['devroe_case'].independent_evidence,INDEPENDENT_EVIDENCE)
            self.assertTrue(r['crystal_truth_independent_of_raven'])
            self.assertNotIn('R5.3_CONSENSUAL_PRIVATE',r['scene_ids'])
            self.assertFalse(r['prehearing_private_intimacy'])
    def test_crystal_fight_paths_have_same_case(self):
        for bits in itertools.product((False,True),repeat=5):
            c=simulate_crystal_screen(bits[0],bits[1],bits[2:])
            self.assertEqual(c['devroe_case'].historical_facts,HISTORICAL_FACTS)
            self.assertEqual(c['devroe_case'].independent_evidence,INDEPENDENT_EVIDENCE)
            self.assertFalse(c['prehearing_private_intimacy'])
            self.assertLess(c['scene_ids'].index('C4.3'), c['scene_ids'].index('C5.1B_E4_RESTORATION_RECORD'))
    def test_early_private_ds_superseded_even_if_posthearing_eligible(self):
        rchoices=RavenChoices(relationship_intent='crystal',crystal_pressure='disclose',
              independently_verified_disclosure=True,raven_free=True,crystal_free=True,
              crystal_reciprocates=True,chooses_ds=True,limits_agreed=True,
              crystal_active_consent=True,raven_active_consent=True)
        r=simulate_raven_screen(False,False,choices=rchoices)
        self.assertIn('R5.3_INFORMED_NO_INTIMACY',r['scene_ids'])
        self.assertIn('R6.5_POSTHEARING_CONSENSUAL_DS',r['scene_ids'])
        cchoices=CrystalChoices(relationship_intent='raven', chooses_private_ds=True,
              raven_reciprocates=True,raven_free=True,crystal_free=True,
              raven_disclosure_verified=True,limits_agreed=True,
              crystal_active_consent=True,raven_active_consent=True)
        c=simulate_crystal_screen(True,True,choices=cchoices)
        self.assertIn('C5.3_INFORMED_NO_INTIMACY',c['scene_ids'])
        self.assertIn('C6.5_POSTHEARING_CONSENSUAL_DS',c['scene_ids'])
    def test_no_preemptive_guilt_or_acquittal(self):
        record=case_for_route(True)
        self.assertTrue(record.kill_order_signer_identified)
        self.assertFalse(record.criminal_verdict_final)
        self.assertFalse(record.rescue_if_restored_proven)
        self.assertTrue(record.raven_disclosure_full)
    def test_evidence_order_before_final_reveal(self):
        r=simulate_raven_screen(True,True,(True,True,True))
        scene=r['scene_ids']
        self.assertLess(scene.index('R5.1B_E4_RESTORATION_RECORD'),scene.index('R6.2'))
        self.assertLess(scene.index('R4.3'),scene.index('R5.1B_E4_RESTORATION_RECORD'))
    def test_no_romance_advantage_in_tournament(self):
        base=simulate_raven_screen(True,True,(True,True,True))
        r=simulate_raven_screen(True,True,(True,True,True),RavenChoices(shuttle_statement='false_denial',crystal_pressure='exploit'))
        self.assertEqual(base['tournament'],r['tournament'])

if __name__=='__main__': unittest.main()
