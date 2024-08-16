from hacker_hank.lisa_workbook import workbook
from pytest import mark


@mark.parametrize("input_array, expected, k", [([100], 100, 1), ([1, 10, 12, 4, 11, 6, 8, 15, 23, 24, 23, 24, 39, 34, 50, 3, 58, 62, 71, 79, 95, 100, 2, 2, 100, 100, 100, 100, 100, 100, 1, 100, 100, 100, 100, 100, 3, 100, 100, 100], 12, 7)])
def test_workbook(input_array, expected, k):
    n = len(input_array)
    output = workbook(n, k, input_array)
    assert output == expected
