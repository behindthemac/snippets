def brute_force(length, characters, string=""):
    """Generate all possible strings with given length from given characters.

    Arguments:
    length -- length of strings
    characters -- characters that form strings

    Generate:
    all possible strings with given length from given characters
    """
    if length > 0:
        for character in characters:
            yield from brute_force(length - 1, characters, string + character)
    else:
        yield string
