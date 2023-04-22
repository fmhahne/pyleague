"""Useful classes and functions to manage league"""

from collections import defaultdict
from dataclasses import dataclass
from typing import Collection, Optional

from rich import box
from rich.table import Table
from rich.text import Text


@dataclass(init=False)
class Match:
    """Holds results for match, and compute useful stats."""

    def __init__(self, teams: tuple[str, str], score: tuple[int, int]):
        if len(teams) != 2 or len(score) != 2:
            raise ValueError("Teams and score must be tuples of length two")

        if teams[0] == teams[1]:
            raise ValueError("Teams must have different names")

        self.teams = teams
        self.score = score

    def result(self, team: str) -> str:
        """Returns string result for `team`"""

        if self.goals_for(team) > self.goals_against(team):
            return "Won"

        if self.goals_for(team) < self.goals_against(team):
            return "Lost"

        return "Drawn"

    def goals_for(self, team: str) -> int:
        """Returns goals scored by `team`"""
        return self.score[self.teams.index(team)]

    def goals_against(self, team: str) -> int:
        """Returns goals scored against `team`"""
        return self.score[self.teams.index(team) - 1]


class League:
    """Holds config and stats for all teams"""

    def __init__(self, config: Optional[dict] = None):
        self.config: dict = {
            "criteria": "Points GD GF".split(),
            "rating": {"initial": 1500.0, "k": 20.0, "advantage": 0.0},
            "points": {"Won": 3, "Drawn": 1, "Lost": 0},
            "styles": {},
        }

        if config is not None:
            self.config.update(config)

        self.teams: dict[str, dict] = {}

    def sort(self, criteria: Optional[Collection[str]] = None) -> None:
        """Sort teams by `criteria`"""

        if criteria is None:
            criteria = self.config["criteria"]

        if criteria is not None:
            self.teams = dict(
                sorted(
                    self.teams.items(),
                    key=lambda t: tuple(t[1][c] for c in criteria),
                    reverse=True,
                )
            )

    def add_match(self, match: Match) -> None:
        """Add match to league stats"""

        for team in match.teams:
            if team not in self.teams:
                self.teams[team] = defaultdict(int)
                self.teams[team]["Rating"] = self.config["rating"]["initial"]

            self.teams[team]["Played"] += 1

            self.teams[team]["GF"] += match.goals_for(team)
            self.teams[team]["GA"] += match.goals_against(team)
            self.teams[team]["GD"] += match.goals_for(team) - match.goals_against(team)

            result = match.result(team)
            self.teams[team][result] += 1
            self.teams[team]["Points"] += self.config["points"][result]

        # Rating computations

        home, away = match.teams
        home_result = {"Won": 1.0, "Drawn": 0.5, "Lost": 0.0}[match.result(home)]
        delta = (
            self.config["rating"]["advantage"]
            + self.teams[home]["Rating"]
            - self.teams[away]["Rating"]
        )
        change = self.config["rating"]["k"] * (
            home_result - 1 / (1 + 10 ** (-delta / 400))
        )

        self.teams[home]["Rating"] += change
        self.teams[away]["Rating"] -= change

    def table(self, columns: Collection[str], **kwargs) -> Table:
        """Returns table from rich with specified `columns`"""

        table = Table(row_styles=["none", "dim"], box=box.SIMPLE_HEAD, **kwargs)

        table.add_column("#", justify="right")
        table.add_column("Name")

        for column in columns:
            table.add_column(column, justify="right")

        for num, (name, team_stats) in enumerate(self.teams.items(), 1):
            if num in self.config["styles"]:
                style = self.config["styles"][num]
            else:
                style = "none"

            num_text = Text(str(num), style=style)

            if name in self.config["styles"]:
                style = style = self.config["styles"][name]
            else:
                style = "none"

            name_text = Text(name, style=style)

            table.add_row(
                num_text, name_text, *[str(round(team_stats[c])) for c in columns]
            )

        return table
