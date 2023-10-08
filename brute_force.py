def brute_force(length, elements, array=[]):
    """Generates all possible arrays from given elements in given length.

    Args:
        length: The length of arrays
        elements: Elements that make up arrays

    Yields:
        All possible arrays that consist of given elements in given length
    """
    if length > 0:
        for element in elements:
            yield from brute_force(length - 1, elements, array + [element])
    else:
        yield array
