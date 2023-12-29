# pyleague

Python package to generate pairings for a round-robin league, and print standings table of existing leagues.

## Installation

Recommended way of installing is using `pip`:

```
pip install git+https://github.com/fernandomhahne/pyleague.git
```

## CLI usage

### Generate pairings

This program can be used to generate pairings for a round-robin league.
The participants names must be listed in a text file, one name per line, as below:

```
Germany
Brazil
Argentina
Italy
```

From this file, the pairings can be generated with:

```
pyleague generate names.txt
```

The result should be:

```
## Round 1

Germany x Italy
Argentina x Brazil

## Round 2

Argentina x Germany
Brazil x Italy

## Round 3

Germany x Brazil
Italy x Argentina

## Round 4

Italy x Germany
Brazil x Argentina

## Round 5

Germany x Argentina
Italy x Brazil

## Round 6

Brazil x Germany
Argentina x Italy
```

It is possible to randomize the results with the `--shuffle` flag.

### Print ranking

The package pyleague also allows the user to get the ranking table from an existing league.

Leagues must be store in a text file, formatted as below.

```
---
points: {Won: 3, Drawn: 1, Lost: 0}
criteria: ["Points", "GD", "GF"]
styles: {1: bold green, 2: bold cyan, 3: bold red, 4: bold red}
---

# 2018 FIFA World Cup, group B

15/jun | Morocco x Iran - 0x1
15/jun | Portugal x Spain - 3x3
20/jun | Portugal x Morocco - 1x0
20/jun | Iran x Spain - 0x1
25/jun | Iran x Portugal - 1x1
25/jun | Spain x Morocco - 2x2
```

The only relevant parts are the front matter configuration and the matches in the format `Home x Away - 2x1`. All the rest is ignored.

To print the ranking table, use:

```
pyleague rank file.txt
```

The result is supposed to look like this:
```
  #   Name       Played   Won   Drawn   Lost   GF   GA   GD   Points
 ────────────────────────────────────────────────────────────────────
  1   Spain           3     1       2      0    6    5    1        5
  2   Portugal        3     1       2      0    5    4    1        5
  3   Iran            3     1       1      1    2    2    0        4
  4   Morocco         3     0       1      2    2    4   -2        1
```

## API usage

This package can be imported as part of another Python program.
See tests for examples.
