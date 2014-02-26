"""
Chi2012 problem
"""

from collections import defaultdict


def check_invariants(land_heights, stops):
    for x, y in enumerate(land_heights):
        if y in stops:
            assert stops[y] < x


def make_stops(land_heights, fire_heights):
    """
    stops[h] -> x location where ball fired at height h stops
    """
    stops = defaultdict(lambda: -1)
    h = 0
    for x, y in enumerate(land_heights):
        while (y >= h):
            # only lookup elements of fire_heights
            if h in fire_heights:
                stops[h] = x - 1
            h += 1
    return stops


def fire(land_heights, fire_heights):
    """
    stops[h] -> x location where a ball fired at h stops
    or -1 if ricochet/leaves system
    """
    stops = make_stops(land_heights, set(fire_heights))
    for h in fire_heights:
        x = stops[h]

        # leaves system
        if x < 0:
            continue

        # update landscape
        land_heights[x] += 1

        assert land_heights[x + 1] >= h

        # update stops array, if needed
        y = land_heights[x]
        if y in stops and stops[y] >= x:
            stops[y] = x - 1

    return land_heights

solution = fire
