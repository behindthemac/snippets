# recursive
def euclidean_algorithm_recursive(a, b):
    """Returns the greatest common divisor of two integers.

    Args:
        a: A positive integer
        b: A positive integer

    Returns:
        The greatest common divisor of the two integers.
    """
    if b != 0:
        return euclidean_algorithm_recursive(b, a % b)
    return a


# iterative
def euclidean_algorithm_iterative(a, b):
    """Returns the greatest common divisor of two integers.

    Args:
        a: A positive integer
        b: A positive integer

    Returns:
        The greatest common divisor of the two integers.
    """
    while b != 0:
        a, b = b, a % b
    return a
