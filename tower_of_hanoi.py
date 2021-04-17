def tower_of_hanoi(disks, fr=0, to=1, sp=2):
    """Solve the Tower of Hanoi.

    Arguments:
    disks -- number of disks
    fr -- rod from which disks are moved
    to -- rod to which disks are moved
    sp -- spare rod

    Generate:
    tuple of indices of rods ((a, b) means moving a disk from rod a to rod b)
    """
    if disks > 1:
        yield from tower_of_hanoi(disks - 1, fr, sp, to)
        yield fr, to
        yield from tower_of_hanoi(disks - 1, sp, to, fr)
    else:
        yield fr, to
