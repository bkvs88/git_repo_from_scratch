import pytest

from addition import add
from division import div
from multiplication import multiply
from power import power
from substraction import sub


@pytest.mark.parametrize(
    ("func", "a", "b", "expected"),
    [
        (add, 10, 4, 14),
        (add, -3, 3, 0),
        (sub, 10, 4, 6),
        (sub, 4, 10, -6),
        (multiply, 10, 4, 40),
        (multiply, -3, 3, -9),
        (power, 2, 10, 1024),
        (power, 5, 0, 1),
    ],
)
def test_operations_return_correct_value(func, a, b, expected):
    assert func(a, b) == expected


@pytest.mark.parametrize("func", [add, sub, multiply, power])
def test_operations_print_a_result_line(func, capsys):
    func(10, 4)
    out = capsys.readouterr().out
    assert out.strip() != ""


def test_division_returns_float():
    assert div(10, 4) == 2.5
    assert div(9, 3) == 3.0


def test_division_by_zero_returns_none(capsys):
    assert div(10, 0) is None
    assert "cannot divide 10 by zero" in capsys.readouterr().out


def test_division_by_zero_does_not_fabricate_a_result(capsys):
    """Regression guard.

    The original div() overwrote both operands (a = 0, b = 1) and printed a
    confident but false "Division of 0 and 1 is : 0.0". It must now report the
    error and leave the real operands alone.
    """
    div(10, 0)
    out = capsys.readouterr().out
    assert "Division of 0 and 1" not in out
    assert "Division of 10 and 0" not in out


def test_operations_return_their_result(capsys):
    """Every operation both prints and returns, so callers can chain them."""
    for func, args, expected in [
        (add, (2, 3), 5),
        (sub, (2, 3), -1),
        (multiply, (2, 3), 6),
        (power, (2, 3), 8),
    ]:
        assert func(*args) == expected
        assert capsys.readouterr().out.strip() != ""
