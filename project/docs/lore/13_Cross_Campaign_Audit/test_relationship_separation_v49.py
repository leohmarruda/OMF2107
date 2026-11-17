import unittest
from world_state import Event,WorldState,StateConflict

class RelationshipSeparationV49Tests(unittest.TestCase):
    def couple(self):
        w=WorldState('Lyra')
        w.apply(Event('a','decision','day0_1','Lyra','Dante',(True,)))
        w.apply(Event('b','decision','day0_1','Dante','Lyra',(True,)))
        w.apply(Event('couple','commit','day0_1','Lyra','Dante'))
        return w
    def test_lyra_can_leave_without_dante_agreeing(self):
        w=self.couple()
        w.apply(Event('lyra_no','decision','group_stage','Lyra','Dante',(False,)))
        w.apply(Event('breakup','separate','group_stage','Lyra','Dante'))
        self.assertEqual(w.bonds,set())
    def test_cannot_separate_without_initiator_decision(self):
        w=self.couple()
        with self.assertRaises(StateConflict):
            w.apply(Event('breakup','separate','group_stage','Lyra','Dante'))
        self.assertEqual(len(w.bonds),1)
    def test_other_person_cannot_use_someone_elses_no(self):
        w=self.couple()
        w.apply(Event('lyra_no','decision','group_stage','Lyra','Dante',(False,)))
        with self.assertRaises(StateConflict):
            w.apply(Event('breakup','separate','group_stage','Dante','Lyra'))
        self.assertEqual(len(w.bonds),1)
    def test_no_need_for_reciprocal_rejection_and_cannot_repeat(self):
        w=self.couple()
        w.apply(Event('lyra_no','decision','group_stage','Lyra','Dante',(False,)))
        w.apply(Event('breakup','separate','group_stage','Lyra','Dante'))
        with self.assertRaises(StateConflict):
            w.apply(Event('breakup_again','separate','group_stage','Lyra','Dante'))
    def test_new_commitment_still_requires_independent_yes(self):
        w=self.couple()
        w.apply(Event('lyra_no','decision','group_stage','Lyra','Dante',(False,)))
        w.apply(Event('breakup','separate','group_stage','Lyra','Dante'))
        w.apply(Event('lyra_yes','decision','group_stage','Lyra','Steffan',(True,)))
        with self.assertRaises(StateConflict):
            w.apply(Event('new','commit','group_stage','Lyra','Steffan'))
        w.apply(Event('steffan_yes','decision','group_stage','Steffan','Lyra',(True,)))
        w.apply(Event('new','commit','group_stage','Lyra','Steffan'))
        self.assertIn(frozenset(('Lyra','Steffan')),w.bonds)

if __name__=='__main__':unittest.main()
