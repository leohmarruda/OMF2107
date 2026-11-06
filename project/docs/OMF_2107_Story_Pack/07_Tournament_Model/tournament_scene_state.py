"""Branch-aware tournament screenplay state, without unapproved canonical decisions."""
from __future__ import annotations

def build_scene_state(result: dict) -> dict:
    matches = {m['id']: m for m in result['matches']}
    pilot = result['selected_pilot']
    reached = {m['id'] for m in result['matches'] if pilot in (m['left'], m['right'])}
    final_winner = result['champion']
    return {
        'selected_pilot': pilot,
        'played_knockout_ids': tuple(i for i in ('Q1', 'Q2', 'Q3', 'Q4', 'S_AB', 'S_CD', 'FINAL') if i in reached),
        'matches_by_id': {k: dict(v) for k, v in matches.items()},
        'final_winner': final_winner,
        'ceremony_presenter_rule': ('independent_awards_official' if final_winner == 'Crystal' else 'Crystal'),
        'final_is_playable': 'FINAL' in reached,
        'champion': result['champion'],
        'finalists': (matches['FINAL']['left'], matches['FINAL']['right']),
        'semifinalists': {k: (matches[k]['left'], matches[k]['right']) for k in ('S_AB','S_CD')},
        'selected_pilot_elimination': result['player_elimination_match'],
        'selected_pilot_is_champion': result['player_champion'],
        'group_rankings': {g: tuple(v['ranked']) for g,v in result['group_standings'].items()},
        'official_tournament_over_before_nova': result['nova_encounter']=='SEPARATE_FROM_OFFICIAL_BRACKET',
        'audit': dict(result['audit']),
    }
