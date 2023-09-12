def element_wise(f):
    """Makes an operation element-wise.

    Args:
        f: A function

    Returns:
        The function whose operation made element-wise
    """
    return lambda *args: [f(*arg) for arg in zip(*args)]
