from rich.text import Text

from pyleague import League, Match

matches = [
    Match(("Morocco", "Iran"), (0, 1)),
    Match(("Portugal", "Spain"), (3, 3)),
    Match(("Portugal", "Morocco"), (1, 0)),
    Match(("Iran", "Spain"), (0, 1)),
    Match(("Iran", "Portugal"), (1, 1)),
    Match(("Spain", "Morocco"), (2, 2)),
]
league = League()
for match in matches:
    league.add_match(match)


def test_config():
    league2 = League(config={"points": {"Won": 6, "Drawn": 2, "Lost": 0}})

    assert league2.config == {
        "criteria": "Points GD GF".split(),
        "rating": {"initial": 1500.0, "k": 20.0, "advantage": 0.0},
        "points": {"Won": 6, "Drawn": 2, "Lost": 0},
        "styles": {},
    }


def test_add_match():
    for team in "Iran Morocco Portugal Spain".split():
        assert team in league.teams


def test_stats():
    assert league.teams["Iran"]["Played"] == 3
    assert league.teams["Iran"]["Won"] == 1
    assert league.teams["Iran"]["Drawn"] == 1
    assert league.teams["Iran"]["Lost"] == 1
    assert league.teams["Iran"]["GF"] == 2
    assert league.teams["Iran"]["GA"] == 2
    assert league.teams["Iran"]["GD"] == 0
    assert league.teams["Iran"]["Points"] == 4


def test_sort():
    league.sort()
    assert list(league.teams.keys()) == "Spain Portugal Iran Morocco".split()


def test_table():
    league.config["styles"][1] = "green"
    league.config["styles"][2] = "cyan"
    league.config["styles"]["Spain"] = "blue"

    columns = "Played GF Points".split()
    table = league.table(columns)
    assert [c.header for c in table.columns] == ["#", "Name"] + columns

    numbers_text = [
        Text("1", style="green"),
        Text("2", style="cyan"),
        Text("3"),
        Text("4"),
    ]
    assert list(table.columns[0].cells) == numbers_text

    teams_text = [
        Text("Spain", style="blue"),
        Text("Portugal"),
        Text("Iran"),
        Text("Morocco"),
    ]
    assert list(table.columns[1].cells) == teams_text
