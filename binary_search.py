def binary_search(array, target):
    """Find an element that matches the target from an array.

    Arguments:
    array: array (must be sorted in ascending order)
    target: target element

    Return:
    index: index of the first element that matches the target
    """
    l = 0
    r = len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] < target:
            l = m + 1
        elif array[m] > target:
            r = m - 1
        else:
            return m
