from pyleague import Match, parser

# 2018 FIFA World Cup, group B
expected_matches = [
    Match(("Morocco", "Iran"), (0, 1)),
    Match(("Portugal", "Spain"), (3, 3)),
    Match(("Portugal", "Morocco"), (1, 0)),
    Match(("Iran", "Spain"), (0, 1)),
    Match(("Iran", "Portugal"), (1, 1)),
    Match(("Spain", "Morocco"), (2, 2)),
]
matches, config = parser.load("tests/example.md")


def test_matches():
    assert matches == expected_matches


def test_config():
    assert config == {"points": {"Won": 6, "Drawn": 2, "Lost": 0}}
