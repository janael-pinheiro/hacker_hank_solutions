from hacker_hank.beautiful_binary_string import beautiful_binary_string
from pytest import mark


@mark.parametrize("b, expected", [
    ("0101010", 2),
    ("01100", 0),
    ("0100101010", 3)])
def test_beautiful_binary_string(b, expected):
    output = beautiful_binary_string(b)
    assert output == expected
