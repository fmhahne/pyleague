import hypothesis.strategies as st
import pytest
from hypothesis import assume, given

from pyleague import Match


@given(st.text(), st.integers(), st.integers())
def test_teams_equal_names(name, score_home, score_away):
    with pytest.raises(ValueError):
        Match((name, name), (score_home, score_away))


@given(st.text(), st.text(), st.integers(), st.integers())
def test_wrong_tuple_length(home, away, score_home, score_away):
    assume(home != away)

    with pytest.raises(ValueError):
        Match((home,), (score_home, score_away))

    with pytest.raises(ValueError):
        Match((home, away), (score_home,))


@given(st.text(), st.text(), st.integers(), st.integers())
def test_result_won_by_home(home, away, score_home, score_away):
    assume(home != away)
    assume(score_home > score_away)
    assert Match((home, away), (score_home, score_away)).result(home) == "Won"
    assert Match((home, away), (score_home, score_away)).result(away) == "Lost"


@given(st.text(), st.text(), st.integers(), st.integers())
def test_result_won_by_away(home, away, score_home, score_away):
    assume(home != away)
    assume(score_home < score_away)
    assert Match((home, away), (score_home, score_away)).result(home) == "Lost"
    assert Match((home, away), (score_home, score_away)).result(away) == "Won"


@given(st.text(), st.text(), st.integers())
def test_result_drawn(home, away, number):
    assume(home != away)
    assert Match((home, away), (number, number)).result(home) == "Drawn"
    assert Match((home, away), (number, number)).result(away) == "Drawn"


@given(st.text(), st.text(), st.integers(), st.integers())
def test_goals_for(home, away, score_home, score_away):
    assume(home != away)
    match = Match((home, away), (score_home, score_away))
    assert match.goals_for(home) == score_home
    assert match.goals_for(away) == score_away


@given(st.text(), st.text(), st.integers(), st.integers())
def test_goals_against(home, away, score_home, score_away):
    assume(home != away)
    match = Match((home, away), (score_home, score_away))
    assert match.goals_against(home) == score_away
    assert match.goals_against(away) == score_home
