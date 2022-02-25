"""Pairing generator for round-robin league"""

from typing import Generator, Optional


def rounds(
    teams: list[str], count: Optional[int] = None
) -> Generator[list[tuple[str, str]], None, None]:
    """ "Yields lists of pairings for each round"""

    if len(teams) % 2 == 1:
        teams.insert(0, None)

    if count is None:
        count = (len(teams) - 1) * 2

    for r_num in range(count):
        pairings = []

        for i in range(len(teams) // 2):
            if teams[i] is not None:
                if (i != 0 and (i + r_num // (len(teams) - 1)) % 2 == 1) or (
                    i == 0 and r_num % 2 == 1
                ):
                    pairings.append((teams[-i - 1], teams[i]))
                else:
                    pairings.append((teams[i], teams[-i - 1]))

        teams = teams[:1] + teams[1:][-1:] + teams[1:][:-1]
        yield pairings
