from hacker_hank.missing_numbers import missing_numbers
from pytest import mark


@mark.parametrize("arr, brr, expected", [
    ([7, 2, 5, 3, 5, 3], [7, 2, 5, 4, 6, 3, 5, 3], [4, 6]),
    ([203, 204, 205, 206, 207, 208, 203, 204, 205, 206], [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204], [204, 205, 206])])
def test_missing_numbers(arr, brr, expected):
    output = missing_numbers(arr, brr)
    assert output == expected
