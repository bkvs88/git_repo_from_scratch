from division import div


def test_div_returns_quotient():
    assert div(10, 4) == 2.5


def test_division_by_zero_returns_none():
    assert div(5, 0) is None
