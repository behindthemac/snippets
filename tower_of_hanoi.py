def tower_of_hanoi(n, fr=0, to=1, sp=2):
    """Solve the Tower of Hanoi.

    Args:
        n: The number of disks
        fr: The label of the rod that the disks are moved from
        to: The label of the rod that the disks are moved to
        sp: The label of the spare rod

    Yields:
        Tuples that represents a move of the disks
    """
    if n > 1:
        yield from tower_of_hanoi(n - 1, fr, sp, to)
        yield fr, to
        yield from tower_of_hanoi(n - 1, sp, to, fr)
    else:
        yield fr, to
