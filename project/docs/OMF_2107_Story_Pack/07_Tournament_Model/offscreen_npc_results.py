"""Read-only tournament-board projection. NPC-versus-NPC fights are NEVER staged.

The projection consumes the existing simulator's 19-match ledger. It cannot
choose winners or scores, and will not present proposal-derived results as canon.
"""
from __future__ import annotations

from tournament_validator import validate

NPC_STAGES = ('Q1', 'Q2', 'Q3', 'Q4', 'S_AB', 'S_CD', 'FINAL')


def project_board(result: dict, *, allow_draft: bool = False) -> dict:
    """Generate UI-safe standings, bracket and dialogue facts.

    For production display, require resolved authored results and score-based
    circular standings. In draft mode every noncanonical fact is labeled.
    A missing match score is represented as null; no numeric score is invented.
    """
    validate(result)
    audit = result.get('audit', {})
    if not allow_draft and not audit.get('canon_ready', False):
        raise ValueError('Tournament has unapproved winner or standings; board is draft-only')
    selected = result['selected_pilot']
    matches = []
    for m in result['matches']:
        involving_player = selected in (m['left'], m['right'])
        classification = 'player_fight' if involving_player else 'npc_offscreen_result'
        proposed = m['resolution'] in ('proposed_npc_pair_PENDING_APPROVAL', 'provisional_npc_priority_NOT_CANON')
        scores = m.get('scores')
        matches.append({
            'id': m['id'], 'stage': 'group' if m['id'].startswith('G') else 'knockout',
            'left': m['left'], 'right': m['right'], 'winner': m['winner'], 'loser': m['loser'],
            'display_kind': classification,
            'render_fight': involving_player,  # NPC matches: scoreboard only
            'scores': dict(scores) if scores is not None else None,
            'score_available': scores is not None,
            'provenance': m['resolution'], 'requires_approval': proposed,
        })
    return {
        'selected_pilot': selected, 'champion': result['champion'],
        'standings': {g: {'ranking': list(s['ranked']), 'wins': dict(s['wins']),
                          'cumulative_scores': s['score_totals'],
                          'ranking_method': s['ranking_method']}
                      for g, s in result['group_standings'].items()},
        'bracket': matches,
        'npc_results': [m for m in matches if m['display_kind'] == 'npc_offscreen_result'],
        'dialogue_bindings': {
            'champion': result['champion'],
            'finalists': (next(m for m in matches if m['id'] == 'FINAL')['left'],
                          next(m for m in matches if m['id'] == 'FINAL')['right']),
            'player_elimination': result['player_elimination_match'],
            'player_champion': result['player_champion'],
        },
        'is_draft': not audit.get('canon_ready', False),
        'requires_author_approval': [m['id'] for m in matches if m['requires_approval']],
        'unresolved_standings': list(audit.get('unapproved_cycle_seed_groups', [])),
    }
