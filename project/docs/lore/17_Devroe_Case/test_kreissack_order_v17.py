"""Kreissack 2092 case order: immutable truth versus 2107 character knowledge."""
import itertools
import unittest
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / '18_Christian_Subplot'))
from devroe_case_state import case_for_route, HISTORICAL_FACTS, INDEPENDENT_EVIDENCE
from christian_secondary_state import christian_secondary_arc, evidence_known_by_christian

class KreissackOrderTests(unittest.TestCase):
    def test_the_human_mastermind_is_fixed_on_every_route(self):
        for disclosure in (False, True):
            record = case_for_route(disclosure)
            self.assertIn('kreissack_personally_authorized_2092_lethal_interception',record.historical_facts)
            self.assertIn('raven_not_briefed_on_kreissack_lethal_contingency',record.historical_facts)
            self.assertIn('nova_not_agent_of_2092_shuttle_attack',record.historical_facts)
            self.assertTrue(record.kill_order_signer_identified)
            self.assertFalse(record.criminal_verdict_final)

    def test_e5_proof_after_default_final_not_before(self):
        for day in (0,5,8,10,11,12,13,29):
            self.assertNotIn(INDEPENDENT_EVIDENCE[-1], evidence_known_by_christian(day))
        self.assertIn(INDEPENDENT_EVIDENCE[-1], evidence_known_by_christian(30))

    def test_murder_order_independent_of_player_raven_and_early_elimination(self):
        for pilot, rv, eliminated in itertools.product(
                ('Ari','Lyra','Mara','Ren','Angel','Crystal','Raven'),
                ('full','selective','false_denial'),(True,False)):
            result=christian_secondary_arc(selected_pilot=pilot, raven_disclosure=rv,
                pilot_eliminated=eliminated)
            self.assertIn(INDEPENDENT_EVIDENCE[-1],result['evidence_by_day'][30])
            self.assertNotIn(INDEPENDENT_EVIDENCE[-1],result['evidence_by_day'][13])
            self.assertIn('CH6.1B_E5_KREISSACK_ORDER',result['scene_ids'])
            self.assertLess(result['scene_ids'].index('CH6.1_POST_FINAL_NOVA_VETO'),
                result['scene_ids'].index('CH6.1B_E5_KREISSACK_ORDER'))
            self.assertLess(result['scene_ids'].index('CH6.1B_E5_KREISSACK_ORDER'),
                result['scene_ids'].index('CH6.2_INDEPENDENT_HEARING'))

if __name__=='__main__': unittest.main()
