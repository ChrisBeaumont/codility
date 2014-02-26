from cannon import fire
from random import randint


def check(a, b, expect):
    assert fire(a, b) == expect


def test_default():
    check([1, 2, 0, 4, 3, 2, 1, 5, 7],
          [2, 8, 0, 7, 6, 5, 3, 4, 5, 6, 5],
          [2, 2, 2, 4, 3, 3, 5, 6, 7])


def test_big():
    land_heights = [randint(0, 1000000) for _ in range(30000)]
    fire_heights = [randint(0, 1000000) for _ in range(30000)]
    fire(land_heights, fire_heights)
