"""Autograding script."""

from click.testing import CliRunner
from homework.myclitool import mycli


def test_c1_s1():
    runner = CliRunner()
    result = runner.invoke(mycli, ["command1", "run", "--a", "1"])
    assert result.exit_code == 0
    assert "---> Ejecutando command 1 subcommand 1: a = 1" in result.output


def test_c1_s2():
    runner = CliRunner()
    result = runner.invoke(mycli, ["command1", "stop", "--b", "2"])
    assert result.exit_code == 0
    assert "---> Ejecutando command 1 subcommand 2: b = 2" in result.output


def test_c2_s1():
    runner = CliRunner()
    result = runner.invoke(mycli, ["command2", "jump", "--c", "3"])
    assert result.exit_code == 0
    assert "---> Ejecutando command 2 subcommand 1: c = 3" in result.output


def test_c2_s2():
    runner = CliRunner()
    result = runner.invoke(mycli, ["command2", "cry", "--d", "4"])
    assert result.exit_code == 0
    assert "---> Ejecutando command 2 subcommand 2: d = 4" in result.output