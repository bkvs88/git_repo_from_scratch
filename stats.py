"""Summary statistics for the two numbers captured by read_data().

Every function follows the convention used by the rest of the project:
print a human-readable line and return the computed value.
"""


def _mean(a, b):
    """Arithmetic mean of two inputs, without printing.

    Shared by mean() and median(): for exactly two numbers the median is
    mathematically identical to the mean, so both delegate here instead of
    duplicating the formula.
    """
    return (a + b) / 2


def mean(a, b):
    """Arithmetic mean of the two inputs."""
    c = _mean(a, b)
    print(f"Mean of {a} and {b} is : {c}")
    return c


def median(a, b):
    """Middle value of the two inputs."""
    c = _mean(a, b)
    print(f"Median of {a} and {b} is : {c}")
    return c


def minimum(a, b):
    """Smaller of the two inputs."""
    c = min(a, b)
    print(f"Minimum of {a} and {b} is : {c}")
    return c


def maximum(a, b):
    """Larger of the two inputs."""
    c = max(a, b)
    print(f"Maximum of {a} and {b} is : {c}")
    return c
