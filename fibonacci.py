# recursive
def fibonacci_recursive(n, memo=None):
    """Returns the n-th Fibonacci number.

    Args:
        n: The index of the Fibonacci number

    Returns:
        The n-th Fibonacci number
    """
    if memo is None:
        memo = {0: 0, 1: 1}

    if n not in memo:
        memo[n] = fibonacci_recursive(n - 2, memo) + fibonacci_recursive(n - 1, memo)

    return memo[n]
