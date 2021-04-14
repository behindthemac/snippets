def mergesort(array):
    """Sort an array in ascending order with mergesort.

    Argument:
    array -- array

    Return:
    array sorted in ascending order
    """
    n = len(array)
    if n <= 1:
        return array

    m = n // 2
    array1 = mergesort(array[:m])
    array2 = mergesort(array[m:])

    sorted_array = []
    while True:
        if array1[0] < array2[0]:
            sorted_array.append(array1.pop(0))
            if not array1:
                return sorted_array + array2
        else:
            sorted_array.append(array2.pop(0))
            if not array2:
                return sorted_array + array1
