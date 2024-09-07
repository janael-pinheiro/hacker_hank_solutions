from hacker_hank.arrays_new_year_chaos import minimum_bribes
from pytest import mark


@mark.parametrize("q, expected", [
    ([2, 1, 5, 3, 4], "3\n"),
    ([1, 2, 5, 3, 7, 8, 6, 4], "7\n"),
    ([2, 5, 1, 3, 4], "Too chaotic\n"),
])
def test_minimum_bribes(q, expected, capsys):
    minimum_bribes(q)
    captured = capsys.readouterr()
    assert captured.out == expected
