from hacker_hank.two_strings import two_strings
from pytest import mark


@mark.parametrize("s1, s2, expected", [
    ("and", "art", "YES"),
    ("be", "cat", "NO"),
    ("hello", "hi", "YES"),
    ("hi", "world", "NO")])
def test_two_strings(s1, s2, expected):
    output = two_strings(s1, s2)
    assert output == expected
