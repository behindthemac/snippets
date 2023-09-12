def element_wise(f):
    """Makes an operation element-wise.

    Args:
        f: A function

    Returns:
        The function whose operation made element-wise
    """
    return lambda *args: [f(*arg) for arg in zip(*args)]


@element_wise
def add(a, b):
    return a + b

a = [0, 2, 4, 6, 8]
b = [1, 3, 5, 7, 9]
c = add(a, b)
print(c)