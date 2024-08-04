from hacker_hank.love_letter_mystery import love_letter_mystery
from pytest import mark


@mark.parametrize("s,expected", [
    ("abc", 2),
    ("abcba", 0),
    ("abcd", 4)])
def test_love_letter_mystery(s, expected):
    output = love_letter_mystery(s)
    assert output == expected
