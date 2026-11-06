"""Provisional v4.6 outcome registry. Not immutable narrative canon.

Runtime preview may use these results; strict final-canon audit remains distinct.
Explicit author decisions supersede older editorial proposals.
"""
from npc_pair_proposals import PROPOSED_PAIR_WINNERS
from npc_author_approved_v45 import AUTHOR_APPROVED_NPC_WINNERS
from tournament_validator import DEFAULT_KNOCKOUT_WINNERS

PROVISIONAL_NPC_WINNERS = {
    pair: winner for pair, winner in PROPOSED_PAIR_WINNERS.items()
    if pair not in DEFAULT_KNOCKOUT_WINNERS and pair not in AUTHOR_APPROVED_NPC_WINNERS
}

def effective_preview_winners():
    return {**DEFAULT_KNOCKOUT_WINNERS, **PROVISIONAL_NPC_WINNERS,
            **AUTHOR_APPROVED_NPC_WINNERS}
