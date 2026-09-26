from stats import maximum, mean, median, minimum


def test_mean():
    assert mean(2, 4) == 3


def test_median():
    assert median(2, 4) == 3


def test_median_delegates_to_mean_for_two_inputs():
    assert median(-5, 3) == mean(-5, 3)


def test_minimum():
    assert minimum(2, 4) == 2


def test_maximum():
    assert maximum(2, 4) == 4


def test_operations_handle_negatives():
    assert mean(-5, 3) == -1
    assert median(-5, 3) == -1
    assert minimum(-5, 3) == -5
    assert maximum(-5, 3) == 3


def test_operations_handle_negatives_reversed():
    assert mean(3, -5) == -1
    assert minimum(3, -5) == -5
    assert maximum(3, -5) == 3


def test_equal_values():
    for a, b in [(0, 0), (7, 7), (-4, -4)]:
        assert mean(a, b) == a
        assert median(a, b) == a
        assert minimum(a, b) == a
        assert maximum(a, b) == a
