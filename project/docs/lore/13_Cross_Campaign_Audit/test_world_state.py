import unittest
from world_state import WorldState, Event, StateConflict, PILOTS

class LedgerTests(unittest.TestCase):
    def test_twelve_pilots(self):
        for pilot in PILOTS: self.assertEqual(WorldState(pilot).pilot,pilot)
    def test_duplicate_and_out_of_order(self):
        w=WorldState('Dante'); w.apply(Event('a','story','day12_rescue',target='nova_rescue'))
        with self.assertRaises(StateConflict): w.apply(Event('a','story','day12_rescue'))
        with self.assertRaises(StateConflict): w.apply(Event('b','story','day11_ab_semifinal'))
    def test_no_draw_and_final_before_boss(self):
        w=WorldState('Ari')
        with self.assertRaises(StateConflict): w.apply(Event('m','match','day13_final',target='FINAL',payload=('Ari','Mara','Draw')))
        with self.assertRaises(StateConflict): w.apply(Event('boss','story','day13_special_nova',target='nova_boss'))
        w.apply(Event('final','match','day13_final',target='FINAL',payload=('Ari','Mara','Ari')))
        w.apply(Event('boss','story','day13_special_nova',target='nova_boss'))
    def test_evidence_not_retrospective(self):
        w=WorldState('Crystal')
        with self.assertRaises(StateConflict): w.apply(Event('c','clue','day9_reveal',actor='Crystal',target='devroe_e5_order',payload=('private record',)))
        w.apply(Event('c','clue','day30_devroe_authentication',actor='Crystal',target='devroe_e5_order',payload=('Christian',)))
        self.assertFalse(w.knows('Crystal','devroe_e5_order','day13_final'))
        self.assertTrue(w.knows('Crystal','devroe_e5_order','epilogue'))
    def test_consent_exclusivity_and_cnm(self):
        w=WorldState('Milano')
        for i,(a,b) in enumerate((('Cossette','Ibrahim'),('Ibrahim','Cossette'),('Cossette','Milano'),('Milano','Cossette'))):
            w.apply(Event(str(i),'decision','day0_1',actor=a,target=b,payload=(True,)))
        w.apply(Event('b1','commit','day0_1',actor='Cossette',target='Ibrahim'))
        with self.assertRaises(StateConflict): w.apply(Event('b2','commit','day0_1',actor='Cossette',target='Milano'))
        w.apply(Event('iapproval','decision','day0_1',actor='Ibrahim',target='Cossette',payload=(True,)))
        w.apply(Event('mcoverage','decision','day0_1',actor='Milano',target='Cossette',payload=(True,)))
        w.apply(Event('cagreement','cnm_agreement','day0_1',actor='Cossette',payload=(('Ibrahim','Milano'),)))
        w.apply(Event('b2','commit','day0_1',actor='Cossette',target='Milano'))
        self.assertEqual(len(w.bonds),2)
    def test_rejected_event_does_not_mutate(self):
        w=WorldState('Mara')
        with self.assertRaises(StateConflict): w.apply(Event('bad','match','day13_final',target='FINAL',payload=('A','B','C')))
        self.assertEqual(w.events,[])
        self.assertEqual(w.matches,{})

if __name__=='__main__': unittest.main()
