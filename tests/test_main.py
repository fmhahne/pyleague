from typer.testing import CliRunner

from pyleague.__main__ import main

runner = CliRunner()


def test_table():
    result = runner.invoke(main, ["table", "tests/example.md"])
    assert "1 Spain 10 3 1 2 0 6 5 1" in " ".join(result.stdout.split())

    result = runner.invoke(main, ["table", "tests/example.md", "--rating"])
    assert "Rating" in result.stdout


def test_generator():
    result = runner.invoke(main, ["generate", "tests/teams.txt", "--shuffle"])

    assert "A x D" in result.stdout
    assert "C x B" in result.stdout
    assert "C x A" in result.stdout
    assert "B x D" in result.stdout
    assert "A x B" in result.stdout
    assert "D x C" in result.stdout
    assert "D x A" in result.stdout
    assert "B x C" in result.stdout
    assert "A x C" in result.stdout
    assert "D x B" in result.stdout
    assert "B x A" in result.stdout
    assert "C x D" in result.stdout

    result = runner.invoke(main, ["generate", "tests/teams.txt", "--count", 5])

    assert "B x A" not in result.stdout
    assert "C x D" not in result.stdout
