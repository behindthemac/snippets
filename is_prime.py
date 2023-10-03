def is_prime(n):
    """Checks if an integer is a prime number or not.

    Args:
        n: A positive integer

    Returns:
        True if the integer is a prime number, False otherwise
    """
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
