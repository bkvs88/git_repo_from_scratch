import pytest

from stats import maximum, mean, median, minimum


def test_mean():
    assert mean(2, 4) == 3


def test_median():
    assert median(2, 4) == 3


def test_minimum():
    assert minimum(2, 4) == 2


def test_maximum():
    assert maximum(2, 4) == 4


def test_operations_handle_negatives():
    assert minimum(-5, 3) == -5
    assert maximum(-5, 3) == 3


def test_division_by_zero_returns_none():
    from division import div

    assert div(5, 0) is None


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (7, 7, 7),
    ],
)
def test_equal_values(a, b, expected):
    assert mean(a, b) == expected
    assert median(a, b) == expected
    assert minimum(a, b) == expected
    assert maximum(a, b) == expected
