def is_kaprekar_number(n):
    """Checks if an integer is a Kaprekar number or not.

    Args:
        n: An integer

    Returns:
        True if the integer is a Kaprekar number, False otherwise
    """
    maximum = int(''.join(sorted(str(n), reverse=True)))
    minimum = int(''.join(sorted(str(n), reverse=False)))
    if maximum - minimum == n:
        return True
    else:
        return False
