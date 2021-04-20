def slope(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (dx * 2)


def derivative(f, dx):
    return lambda x: slope(f, x, dx)
