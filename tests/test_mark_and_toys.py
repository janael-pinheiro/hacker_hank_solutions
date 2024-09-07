from hacker_hank.mark_and_toys import maximum_toys
from pytest import mark


@mark.parametrize("prices, k, expected", [
    ([1, 2, 3, 4], 7, 3),
])
def test_maximum_toys(prices, k, expected):
    output = maximum_toys(prices, k)
    assert output == expected
