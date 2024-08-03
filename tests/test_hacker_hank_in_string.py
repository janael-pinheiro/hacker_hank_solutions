from hacker_hank.hacker_hank_in_string import hacker_hank_in_string
from pytest import mark


@mark.parametrize("input_data, expected", [
    ("haacckkerrannkk", "YES"),
    ("haacckkerannk", "NO"),
    ("hccaakkerrannkk", "NO"),
    ("hereiamstackerrank", "YES"),
    ("hackerworld", "NO")])
def test_hacker_hank_in_string(input_data, expected):
    output = hacker_hank_in_string(input_data)
    assert output == expected
