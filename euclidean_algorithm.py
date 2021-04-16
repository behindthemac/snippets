def euclidean_algorithm(a, b):
    """Get the greatest common divisor of two integers.

    Arguments:
    a -- positive integer
    b -- positive integer

    Return:
    greatest common divisor of the two integers
    """
    if b != 0:
        return euclidean_algorithm(b, a % b)
    else:
        return a
