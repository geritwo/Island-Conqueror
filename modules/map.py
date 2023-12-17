map_terrain = [
    [1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

capital_location = (3, 2)  # Capital location X, Y


def get_tile(x, y):
    return map_terrain[y][x]


