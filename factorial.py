def factorial(n):
    """Return the factorial of a non-negative integer.

    Argument:
    n -- a non-negative integer
    """
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1
