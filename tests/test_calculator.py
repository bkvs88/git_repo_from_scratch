import builtins

import pytest

import calculator
from readdata import read_data


def test_read_data_parses_two_integers(monkeypatch):
    answers = iter(["10", "4"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    assert read_data() == (10, 4)


def test_read_data_accepts_negative_numbers(monkeypatch):
    answers = iter(["-3", "7"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    assert read_data() == (-3, 7)


def test_read_data_confirms_capture(monkeypatch, capsys):
    answers = iter(["1", "2"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    read_data()
    assert "Data Capture completed" in capsys.readouterr().out


def test_read_data_rejects_non_numeric_input(monkeypatch):
    answers = iter(["abc", "2"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    with pytest.raises(ValueError):
        read_data()


def test_main_runs_all_five_operations(monkeypatch, capsys):
    answers = iter(["10", "4"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    calculator.main()
    out = capsys.readouterr().out
    assert "Basic Calculator" in out
    assert "Addition of 10 and 4 is : 14" in out
    assert "substraction of 10 and 4 is : 6" in out
    assert "Division of 10 and 4 is : 2.5" in out
    assert "multiplication of 10 and 4 is : 40" in out
    assert "Power of 10 raised to 4 is : 10000" in out


def test_main_survives_division_by_zero(monkeypatch, capsys):
    """A zero divisor must not abort the remaining operations."""
    answers = iter(["10", "0"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(answers))
    calculator.main()
    out = capsys.readouterr().out
    assert "cannot divide 10 by zero" in out
    assert "multiplication of 10 and 0 is : 0" in out
    assert "Power of 10 raised to 0 is : 1" in out


def test_entry_point_is_guarded():
    """`python calculator.py` must run main(), but importing must not."""
    source = open(calculator.__file__).read()
    assert 'if __name__ == "__main__":' in source
