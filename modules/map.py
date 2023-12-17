MAP_BASE_TERRAIN = [
    [1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

CAPITAL_LOCATION = (2, 1)  # Capital location X, Y
static_overlay = [
    {'type': 'capital', 'location': CAPITAL_LOCATION}
]
dynamic_overlay = [
    {'type': 'ship', 'location': (2, 2)}
]


def map_handler():
    map_overlay = MAP_BASE_TERRAIN
    for item in static_overlay:
        map_overlay[item['location'][1]][item['location'][0]] = item['type']
    for item in dynamic_overlay:
        map_overlay[item['location'][1]][item['location'][0]] = item['type']

    return map_overlay

