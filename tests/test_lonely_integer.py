from hacker_hank.lonely_integer import lonely_integer
from pytest import mark


@mark.parametrize("a, expected", [
    ([1, 2, 3, 4, 3, 2, 1], 4),
    ([1], 1),
    ([1, 1, 2], 2)])
def test_lonely_integer(a, expected):
    output = lonely_integer(a)
    assert output == expected
