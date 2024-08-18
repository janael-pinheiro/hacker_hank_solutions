from hacker_hank.find_the_median import find_the_median
from pytest import mark


@mark.parametrize("arr, expected", [
    ([5, 3, 1, 2, 4], 3),
    ([0, 1, 2, 4, 6, 5, 3], 3)
])
def test_find_median(arr, expected):
    output = find_the_median(arr)
    assert output == expected
