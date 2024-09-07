from hacker_hank.bubble_sort import count_swaps
from pytest import mark


@mark.parametrize("a, expected", [
    ([1, 2, 3], "Array is sorted in 0 swaps.\nFirst Element: 1\nLast Element: 3\n"),
    ([6, 4, 1], "Array is sorted in 3 swaps.\nFirst Element: 1\nLast Element: 6\n"),
    ([3, 2, 1], "Array is sorted in 3 swaps.\nFirst Element: 1\nLast Element: 3\n")
])
def test_count_swaps(a, expected, capsys):
    count_swaps(a)
    captured = capsys.readouterr()
    assert captured.out == expected

