from islands import solution


def test_ex():
    assert solution([2, 1, 3, 2, 3], [0, 1, 2, 3, 1]) == [1, 2, 2, 0, 2]


def test_single():
    assert solution([2], [1, 2, 3]) == [1, 0, 0]


def test_plateau():
    assert solution([2, 2, 2], [1, 2, 3]) == [1, 0, 0]
