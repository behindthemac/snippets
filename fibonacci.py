def fibonacci(n):
    """Return the n-th Fibonacci number.

    Argument:
    n -- index of the Fibonacci number
    """
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
