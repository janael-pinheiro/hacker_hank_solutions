from pytest import mark
from hacker_hank.marc_cakewalk import macs_cake_walk


@mark.parametrize("calorie, expected", [
    ([5, 10, 7], 44),
    ([1, 3, 2], 11),
    ([7, 4, 9, 6], 79)
])
def test_marc_cake_walk(calorie, expected):
    output = macs_cake_walk(calorie)
    assert expected == output
