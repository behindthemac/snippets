def quicksort(array):
    """Sort an array in ascending order with quicksort.

    Argument:
    array -- array

    Return:
    array sorted in ascending order
    """
    n = len(array)
    if n <= 1:
        return array

    pivot = array[0]
    array1 = []
    array2 = []
    for i in range(1, n):
        if array[i] < pivot:
            array1.append(array[i])
        else:
            array2.append(array[i])

    return quicksort(array1) + [pivot] + quicksort(array2)
