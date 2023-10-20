from euclidean_algorithm import euclidean_algorithm


def is_coprime(a, b):
    """Checks if two integers are coprime or not.

    Args:
        a: An integer
        b: An integer

    Returns:
        True if the integers are coprime, False otherwise
    """
    if euclidean_algorithm(a, b) == 1:
        return True
    return False
