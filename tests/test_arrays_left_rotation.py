from hacker_hank.arrays_left_rotation import rot_left
from pytest import mark


@mark.parametrize("a, d, expected", [
    ([1, 2, 3, 4, 5], 4, [5, 1, 2, 3, 4]),
    ([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10, [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77])
])
def test_rot_left(a, d, expected):
    output = rot_left(a, d)
    assert output == expected
