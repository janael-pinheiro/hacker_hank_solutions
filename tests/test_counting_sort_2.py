from hacker_hank.counting_sort_2 import counting_sort_2
from pytest import mark


@mark.parametrize("arr, expected", [
    ([1, 1, 3, 2, 1], [1, 1, 1, 2, 3])
])
def test_counting_sort_2(arr, expected):
    output = counting_sort_2(arr)
    assert output == expected
