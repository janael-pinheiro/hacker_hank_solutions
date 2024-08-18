from hacker_hank.quicksort_1_partition import quick_sort_1_partition
from pytest import mark


@mark.parametrize("arr, expected", [
    ([4, 5, 3, 7, 2], [3, 2, 4, 5, 7])
])
def test_quick_1_partition(arr, expected):
    output = quick_sort_1_partition(arr)
    assert output == expected
