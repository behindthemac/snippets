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
        return euclidean_algorithm(b, a % b)
    return a
