def slope(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (dx * 2)


def derivative(f, dx):
    return lambda x: slope(f, x, dx)


def definite_integral(f, a, b, dx):
    n = int((b - a) / dx)
    x = [a + dx * i for i in range(n)]
    return sum([f(x_i) for x_i in x]) * dx
