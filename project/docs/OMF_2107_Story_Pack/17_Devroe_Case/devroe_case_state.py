"""Historical Devroe case flags: story truth fixed, evidence independently discoverable.

This is not a judicial verdict and does not model psychological consent.
"""
from dataclasses import dataclass

HISTORICAL_FACTS = (
    '2092_shuttle_luna_to_earth_both_devroe_parents_only_passengers',
    'human_contractor_deliberate_flight_control_sabotage_direct_cause',
    'raven_authorized_illicit_distress_relay_hold_knowing_passengers',
    'raven_received_restoration_request_and_did_not_release_hold',
    'raven_postevent_record_falsification_and_concealment',
    'raven_not_informed_of_lethal_code_before_launch',
    'nova_not_agent_of_2092_shuttle_attack',
    'kreissack_personally_authorized_2092_lethal_interception',
    'raven_not_briefed_on_kreissack_lethal_contingency',
)
INDEPENDENT_EVIDENCE = (
    'E1_civilian_custody_gap',
    'E2_licensing_insurer_relay_hold_signed_by_raven',
    'E3_forensic_malicious_flight_command_iron_fist_contractor_trace',
    'E4_crew_emergency_restoration_request_received_unacted_on',
    'E5_independent_kreissack_signed_lethal_order_and_matched_contractor_ledger',
)

@dataclass(frozen=True)
class DevroeRecord:
    historical_facts: tuple[str,...] = HISTORICAL_FACTS
    independent_evidence: tuple[str,...] = INDEPENDENT_EVIDENCE
    kill_order_signer_identified: bool = True
    criminal_verdict_final: bool = False
    rescue_if_restored_proven: bool = False
    raven_disclosure_full: bool = False


def case_for_route(raven_disclosure_full: bool = False) -> DevroeRecord:
    return DevroeRecord(raven_disclosure_full=raven_disclosure_full)
