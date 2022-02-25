"""Parsers from file to match list"""

import frontmatter

from .league import Match


def load(filepath: str) -> tuple[list[Match], dict]:
    """Use when `filepath` is a text file and matches are formatted as

    ```
    Brazil x Germany - 1x7
    ```

    When there is extra info, as a penalty shoot-out, it will be ignored;
    Therefore
    ```
    Italy x Brazil - 0x0 (p. 2x3)
    ```
    renders as
    ```
    Match(('Italy', 'Brazil'), (0, 0))
    ```
    """

    file = frontmatter.load(filepath)
    config = file.metadata

    matches = []
    for line in file.content.splitlines():
        if " - " in line:
            teams, score = line.strip().split(" | ")[-1].split(" - ")
            teams = tuple(teams.split(" x "))
            score = tuple(int(x.split()[0]) for x in score.split("x")[0:2])
            matches.append(Match(teams, score))

    return matches, config
