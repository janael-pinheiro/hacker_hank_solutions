from hacker_hank.string_construction import string_construction
from pytest import mark


@mark.parametrize("s, expected", [
    ("abcabc", 3),
    ("abcd", 4),
    ("aabdea", 4)])
def test_string_construction(s, expected):
    output = string_construction(s)
    assert output == expected
