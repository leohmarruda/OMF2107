"""One shared finale eligibility contract across POVs: no playthrough creates another core."""
from dataclasses import dataclass
from typing import Literal

PILOTS = ('Ari','Lyra','Mara','Ren','Angel','Crystal','Raven')
REQUIRED_TERMINAL = ('G_damaged','R_isolated','B_to_L_intact','D_irreversible','E_pending','no_complete_backup')

@dataclass(frozen=True)
class FinaleState:
    pilot: str
    day: int
    official_final_finished: bool
    rescue_verified: bool
    attempted_isolation_failed: bool
    composite_revealed: bool
    special_nova_victory: bool
    g_damaged: bool
    r_isolated: bool
    b_to_l_intact: bool
    d_irreversible: bool
    e_pending: bool
    complete_backup: bool = False

def terminal_k6_allowed(s: FinaleState) -> bool:
    return (s.pilot in PILOTS and s.day == 13 and s.official_final_finished
            and s.rescue_verified and s.attempted_isolation_failed
            and s.composite_revealed and s.special_nova_victory
            and s.g_damaged and s.r_isolated and s.b_to_l_intact
            and s.d_irreversible and s.e_pending and not s.complete_backup)

def e5_proof_allowed(day: int, authenticated: bool) -> bool:
    return day >= 30 and authenticated
