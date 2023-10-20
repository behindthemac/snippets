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


# example

length = 4
elements = [0, 1]
for array in brute_force(length, elements):
    print(array)

# output
# [0, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [0, 1, 0, 0]
# [0, 1, 0, 1]
# [0, 1, 1, 0]
# [0, 1, 1, 1]
# [1, 0, 0, 0]
# [1, 0, 0, 1]
# [1, 0, 1, 0]
# [1, 0, 1, 1]
# [1, 1, 0, 0]
# [1, 1, 0, 1]
# [1, 1, 1, 0]
# [1, 1, 1, 1]
