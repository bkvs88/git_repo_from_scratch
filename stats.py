"""Summary statistics for the two numbers captured by read_data().

Every function follows the convention used by the rest of the project:
print a human-readable line and return the computed value.
"""


def mean(a, b):
    """Arithmetic mean of the two inputs."""
    c = (a + b) / 2
    print(f"Mean of {a} and {b} is : {c}")
    return c


def median(a, b):
    """Middle value of the two inputs.

    For exactly two numbers the median is mathematically identical to the
    mean, so this delegates to mean() to keep a single implementation.
    """
    return mean(a, b)


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
