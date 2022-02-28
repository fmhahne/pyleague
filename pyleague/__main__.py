#!/usr/bin/env python
"""CLI tool to manage leagues"""

import random
from typing import Optional

import typer
from rich.console import Console

from . import League, parser, rounds

main = typer.Typer()


@main.command()
def table(
    filepaths: list[str],
    rating: bool = typer.Option(False, help="Prints rating table."),
) -> None:
    """Prints ranking table"""
    league = League()

    for filepath in filepaths:
        matches, config = parser.load(filepath)
        league.config.update(config)

        for match in matches:
            league.add_match(match)

    if rating:
        columns = ["Rating"]
        league.sort(["Rating"])
    else:
        columns = "Points Played Won Drawn Lost GF GA GD".split()
        league.sort()

    console = Console()
    console.print(league.table(columns))


@main.command()
def generate(
    filepath: str,
    count: Optional[int] = typer.Option(None, help="Number of rounds"),
    shuffle: bool = typer.Option(False, help="Shuffles teams and matches"),
):
    """Prints formatted league file"""

    with open(filepath, encoding="utf-8") as file:
        teams = [line.strip() for line in file.readlines()]

    if shuffle:
        random.shuffle(teams)

    for i, matches in enumerate(rounds(teams, count), 1):
        print("## Round", i)
        print()

        if shuffle:
            random.shuffle(matches)

        for match in matches:
            print(match[0], "x", match[1])

        print()


if __name__ == "__main__":
    main()
