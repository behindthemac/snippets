def linear_search(array, target):
    """Find an element that matches the target from an array.

    Arguments:
    array: array
    target: target element

    Return:
    index: index of the first element that matches the target
    """
    for index, value in enumerate(array):
        if value == target:
            return index
