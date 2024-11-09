from hacker_hank.luck_balance import luck_balance
from pytest import mark


@mark.parametrize("k, contests, expected", [
    (3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]], 29)
])
def test_luck_balance(k, contests, expected):
    output = luck_balance(k, contests)
    assert expected == output
