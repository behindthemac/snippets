# recursive
def factorial_recursive(n):
    """Returns the factorial of a non-negative integer.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of the non-negative integer
    """
    if n > 0:
        return n * factorial_recursive(n - 1)
    return 1


# iterative
import functools


def factorial_iterative(n):
    """Returns the factorial of a non-negative integer.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of the non-negative integer
    """
    return functools.reduce(lambda a, b: a * b, [i for i in range(1, n + 1)], 1)
