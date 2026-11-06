"""Regression and eligibility tests for cross-pilot K3/K4/K5/K6 screenplay integration."""
from pathlib import Path
import importlib.util
import pytest

ROOT=Path(__file__).resolve().parents[1]
PILOT_FILES={
    'Lyra':'09_Lyra_Campaign/Lyra_Playable_Screenplay_v0.2.md',
    'Mara':'10_Mara_Campaign/Mara_Playable_Screenplay_v0.2.md',
    'Ren':'11_Ren_Campaign/Ren_Playable_Screenplay_v0.2.md',
    'Angel':'12_Angel_Campaign/Angel_Playable_Screenplay_v0.2.md',
    'Crystal':'15_Crystal_Campaign/OMF_2107_Crystal_Playable_Screenplay_v0.6.md',
    'Raven':'16_Raven_Campaign/OMF_2107_Raven_Playable_Screenplay_v0.5.md',
}
M=ROOT/'19_Kreissack_Arc/pov_integration_v19.py'
spec=importlib.util.spec_from_file_location('pov_integration_v19',M)
mod=importlib.util.module_from_spec(spec)
import sys
sys.modules[spec.name]=mod
spec.loader.exec_module(mod)

def valid(pilot):
    return mod.FinaleState(pilot,13,True,True,True,True,True,True,True,True,True,True,False)

@pytest.mark.parametrize('pilot',PILOT_FILES)
def test_four_ordered_inserts_and_shared_ending(pilot):
    text=(ROOT/PILOT_FILES[pilot]).read_text()
    key={'Lyra':'L','Mara':'M','Ren':'N','Angel':'A','Crystal':'C','Raven':'R'}[pilot]
    indices=[text.index(f'[v1.9 / K{scene}-{key}') for scene in (3,4,5,6)]
    assert indices==sorted(indices), (pilot,indices)
    assert 'Apparently, I can still surprise you.' in text
    assert 'Day 30' in text or 'Day-30' in text
    assert text.index('[v1.9 / K5-') < text.index('[v1.9 / K6-')
    assert 'B→L' in text and 'G' in text and 'R' in text

@pytest.mark.parametrize('pilot',PILOT_FILES)
def test_finale_requires_same_guarded_physical_facts(pilot):
    s=valid(pilot)
    assert mod.terminal_k6_allowed(s)
    from dataclasses import replace
    for field in ('special_nova_victory','g_damaged','r_isolated','b_to_l_intact','d_irreversible','e_pending','attempted_isolation_failed','official_final_finished'):
        assert not mod.terminal_k6_allowed(replace(s,**{field:False})),(pilot,field)
    assert not mod.terminal_k6_allowed(replace(s,complete_backup=True))
    assert not mod.terminal_k6_allowed(replace(s,day=12))
    assert not mod.terminal_k6_allowed(replace(s,day=30))

@pytest.mark.parametrize('pilot',PILOT_FILES)
def test_audience_cutaway_not_an_exclusive_early_clue(pilot):
    text=(ROOT/PILOT_FILES[pilot]).read_text()
    part=text[text.index('[v1.9 / K3-'):text.index('[v1.9 / K4-')]
    assert ('CUTAWAY' in part.upper())
    assert ('private' in part.lower() or 'audience' in part.lower())

@pytest.mark.parametrize('day,authenticated,expected',[(12,False,False),(13,True,False),(29,True,False),(30,False,False),(30,True,True),(35,True,True)])
def test_e5_independent_knowledge_clock(day,authenticated,expected):
    assert mod.e5_proof_allowed(day,authenticated)==expected


def test_raven_participation_requires_external_authorization():
    t=(ROOT/PILOT_FILES['Raven']).read_text()
    assert 'only if' in t[t.index('[v1.9 / K5-R'):t.index('[v1.9 / K6-R')]
    assert 'an authorized pilot' in t


def test_base_ari_finale_preserved():
    t=(ROOT/'04_Screenplay_Reconstructions/Chapter_06_One_Must_Fall_v0.4.md').read_text()
    assert 'Apparently, I can still surprise you.' in t
    assert '[v1.9 / K6-' not in t


def test_integrated_versions_do_not_replace_original_sources():
    for pilot,path in PILOT_FILES.items():
        folder=(ROOT/path).parent
        assert len([f for f in folder.glob('*Screenplay*.md') if f.name!=Path(path).name])>=1,pilot
