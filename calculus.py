def slope(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (dx * 2)
