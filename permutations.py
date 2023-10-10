def permutations(array, permutation=[]):
    """Generates all possible permutations of an array.

    Args:
        array: An array

    Yields:
        All possible permutations of the array
    """
    if array:
        n = len(array)
        for index in range(n):
            value = array.pop(index)
            yield from permutations(array, permutation + [value])
            array.insert(index, value)
    else:
        yield permutation
