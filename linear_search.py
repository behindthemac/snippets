def linear_search(array, target):
    """Gets the index of an element that matches the given target.

    Args:
        array: An array
        target: A target element to search for

    Returns:
        The index of an element that matches the target.
    """
    for index, value in enumerate(array):
        if value == target:
            return index
