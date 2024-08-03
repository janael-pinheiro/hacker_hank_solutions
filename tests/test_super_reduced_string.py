from hacker_hank.super_reduced_string import super_reduced_string
from pytest import mark


@mark.parametrize("s, expected", [
    ("aab", "b"),
    ("abba", "Empty String"),
    ("aaabccddd", "abd"),
    ("aa", "Empty String"),
    ("baab", "Empty String")])
def test_super_reduced_string(s, expected):
    output = super_reduced_string(s)
    assert output == expected
