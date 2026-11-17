import unittest
from finale_flow import route, validate_event_sequence, FinaleConflict, PILOTS
SEQ=('FINAL_COMPLETE','EMERGENCY_AUTHORIZED','G_DAMAGED','R_ISOLATED','D_IRREVERSIBLE','E_EJECTION_STARTED','B_L_ENGAGED','CORE_DESTROYED','EVACUATED')
class FinaleFlowTests(unittest.TestCase):
 def test_all_twelve_cleared_routes(self):
  for p in PILOTS:
   with self.subTest(pilot=p):
    a=route(p,final_complete=True,cleared=True)
    self.assertEqual(a.gateway_actor,p)
    self.assertEqual(a.mode,'player_boss')
    validate_event_sequence(SEQ,a)
 def test_raven_noncombat_map_and_fallback(self):
  for verified, sent, expected in [(True,True,'verify_extract_transmit_map'),(False,False,'independent_survey_fallback'),(True,False,'independent_survey_fallback')]:
   a=route('Raven',final_complete=True,cleared=False,map_verified=verified,map_transmitted=sent)
   self.assertEqual(a.player_action,expected)
   self.assertEqual(a.gateway_actor,'independently_cleared_NPC')
   validate_event_sequence(SEQ,a)
 def test_denied_clearance_is_not_overridden(self):
  for p in PILOTS-{'Raven'}:
   with self.assertRaises(FinaleConflict):route(p,final_complete=True,cleared=False)
 def test_reject_early_and_invalid_access(self):
  for args in [dict(pilot='Raven',final_complete=False,cleared=True),dict(pilot='Raven',final_complete=True,cleared=False,map_transmitted=True),dict(pilot='Dante',final_complete=True,cleared=True,map_verified=True)]:
   with self.assertRaises(FinaleConflict): route(**args)
 def test_order_constraints(self):
  a=route('Selene',final_complete=True,cleared=True)
  for seq in (SEQ[1:]+SEQ[:1],SEQ[:4]+('B_L_ENGAGED',)+SEQ[4:7]+SEQ[8:],SEQ+('G_DAMAGED',)):
   with self.assertRaises(FinaleConflict):validate_event_sequence(seq,a)
if __name__=='__main__':unittest.main()
