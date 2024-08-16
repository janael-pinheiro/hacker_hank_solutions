from hacker_hank.mars_exploration import mars_exploration
from pytest import mark


@mark.parametrize("input_string, expected", [("SOSTOT", 2), ("SOSSPSSQSSOR", 3)])
def test_mars_exploration(input_string, expected):
    output = mars_exploration(input_string)
    assert output == expected
