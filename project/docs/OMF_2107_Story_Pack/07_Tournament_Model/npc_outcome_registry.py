"""Production release gate for deterministic NPC knockout outcomes.

No pending proposal is promoted implicitly. Overrides supply individually
approved pair winners; the seven established exact-pair results are immutable.
"""
from __future__ import annotations

from tournament_validator import DEFAULT_KNOCKOUT_WINNERS
from npc_pair_reachability import reachability


def audit_approved_overrides(approved: dict[frozenset, str]) -> dict:
    if not isinstance(approved, dict):
        raise ValueError('Approved outcomes must be a pair-to-winner dictionary')
    reachable = set(reachability())
    for pair, winner in approved.items():
        if not isinstance(pair, frozenset) or pair not in reachable or winner not in pair:
            raise ValueError(f'Invalid approved matchup: {pair!r} -> {winner!r}')
        if pair in DEFAULT_KNOCKOUT_WINNERS and winner != DEFAULT_KNOCKOUT_WINNERS[pair]:
            raise ValueError(f'Cannot override established cinematic winner: {pair!r}')
    resolved = dict(DEFAULT_KNOCKOUT_WINNERS)
    resolved.update(approved)
    pending = sorted((tuple(sorted(x)) for x in reachable - set(resolved)))
    return {'total_reachable_pairs': len(reachable), 'resolved_pairs': len(resolved),
            'pending_pairs': pending, 'ready_for_production': not pending}


def require_complete_npc_table(approved: dict[frozenset, str]) -> dict:
    status = audit_approved_overrides(approved)
    if not status['ready_for_production']:
        raise ValueError(f"{len(status['pending_pairs'])} reachable NPC pairings lack approved winners")
    return {**DEFAULT_KNOCKOUT_WINNERS, **approved}


def approved_author_outcomes() -> dict[frozenset, str]:
    """Only the eight explicit v4.5 author decisions; excludes proposals."""
    from npc_author_approved_v45 import AUTHOR_APPROVED_NPC_WINNERS
    audit_approved_overrides(AUTHOR_APPROVED_NPC_WINNERS)
    return dict(AUTHOR_APPROVED_NPC_WINNERS)


def current_author_approval_status() -> dict:
    return audit_approved_overrides(approved_author_outcomes())


def provisional_preview_status() -> dict:
    """Complete playable-default table with explicit provenance, not final signoff."""
    from npc_provisional_v46 import PROVISIONAL_NPC_WINNERS, effective_preview_winners
    complete = require_complete_npc_table({**PROVISIONAL_NPC_WINNERS, **approved_author_outcomes()})
    assert complete == effective_preview_winners()
    return {'total_pairs': len(complete), 'cinematic_canon': len(DEFAULT_KNOCKOUT_WINNERS),
            'explicit_author_approved': len(approved_author_outcomes()),
            'provisionally_approved': len(PROVISIONAL_NPC_WINNERS),
            'playable_default_ready': True, 'final_canon_signed_off': False,
            'winners': complete}
