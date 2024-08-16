from hacker_hank.fair_rations import fair_rations

from pytest import mark


@mark.parametrize("input_array, expected", [([2, 3, 4, 5, 6], '4'), ([1, 2], 'NO'), ([2, 4, 3], 'NO'), ([2, 3, 4], 'NO')])
def test_fair_rations(input_array, expected):
    output = fair_rations(input_array)
    assert expected == output
