def paths(x, y):  # Simple recursive solution to find how many paths there are from x to y in a hex grid.
    if x == 0 or y == 0:
        return 1
    return paths(x - 1, y) + paths(x, y - 1) + paths(x - 1, y - 1)
print(paths(1, 10))
