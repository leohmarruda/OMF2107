"""Small continuity contract for Kreissack scene eligibility.

Do not interpret fictional Nova psychology or moral responsibility as a binary
simulation. This only enforces documented event/knowledge and hardware gates.
"""
from dataclasses import dataclass

PILOTS = ('Ari', 'Lyra', 'Mara', 'Ren', 'Angel', 'Crystal', 'Raven')

@dataclass(frozen=True)
class KreissackSceneState:
    day: int
    selected_pilot: str = 'Ari'
    survival_discovered: bool = False
    rescue_verified: bool = False
    relay_activation_started: bool = False
    attempted_isolation_failed: bool = False
    composite_revealed: bool = False
    boss_defeated: bool = False
    gateway_damaged: bool = False
    bio_safety_path_intact: bool = True
    destruction_irreversible: bool = False
    core_ejection_pending: bool = False
    complete_backup_exists: bool = False
    nova_destroyed: bool = False
    e5_authenticated: bool = False


def validate(state: KreissackSceneState) -> None:
    if state.selected_pilot not in PILOTS:
        raise ValueError('unknown selected pilot')
    if state.day < 0:
        raise ValueError('negative day')
    if state.survival_discovered and state.day < 10:
        raise ValueError('survival knowledge too early for main story')
    if state.rescue_verified and state.day < 12:
        raise ValueError('rescue before Act IV')
    if any((state.relay_activation_started, state.attempted_isolation_failed,
            state.composite_revealed, state.boss_defeated,
            state.gateway_damaged, state.destruction_irreversible,
            state.core_ejection_pending, state.nova_destroyed)) and state.day < 13:
        raise ValueError('Day-13 mechanism present too early')
    if state.attempted_isolation_failed and not state.relay_activation_started:
        raise ValueError('isolation failure requires relay activation')
    if state.boss_defeated and not state.relay_activation_started:
        raise ValueError('Nova fight requires the initiated relay crisis')
    if state.e5_authenticated and state.day < 30:
        raise ValueError('E5 kill-order proof cannot be authenticated before Day 30')
    if state.nova_destroyed and not state.boss_defeated:
        raise ValueError('default Nova destruction requires special boss defeat')


def available_scenes(s: KreissackSceneState) -> tuple[str, ...]:
    validate(s)
    out = []
    if s.survival_discovered and s.day >= 10:
        out.append('K1_ARCHIVAL_RECOVERY')
    if s.day >= 13 and s.composite_revealed:
        out.append('K2_RETROSPECTIVE_REPLAY')
    if s.day == 12 and s.rescue_verified and not s.composite_revealed:
        out.append('K3_RESCUE_REFLECTION')
    if s.day == 13 and not s.relay_activation_started:
        out.append('K4_PREACTIVATION_BARGAIN')
    if (s.day == 13 and s.attempted_isolation_failed
            and not s.composite_revealed):
        out.append('K5_FAILED_COMMAND')
    if (s.day == 13 and s.boss_defeated and s.gateway_damaged
            and s.bio_safety_path_intact and s.destruction_irreversible
            and s.core_ejection_pending and not s.complete_backup_exists):
        out.append('K6_HARDWIRED_LAST_CHOICE')
    if s.day >= 30 and s.e5_authenticated:
        out.append('K0_2092_FLASHBACK_POST_E5')
    if s.day >= 30 and s.e5_authenticated and s.nova_destroyed:
        out.append('K7_TWO_TRUTHS_POSTSCRIPT')
    return tuple(out)
