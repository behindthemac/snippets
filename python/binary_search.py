def binary_search(array, target):
    """Gets the index of an element that matches the given target.

    Args:
        array: An array sorted in ascending order
        target: A target element to search for

    Returns:
        The index of an element that matches the target.
    """
    l = 0
    r = len(array)
    while l <= r:
        m = (l + r) // 2
        if array[m] < target:
            l = m + 1
        elif array[m] > target:
            r = m - 1
        else:
            return m
