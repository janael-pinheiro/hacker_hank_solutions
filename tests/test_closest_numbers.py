from hacker_hank.closest_numbers import closest_numbers
from pytest import mark


@mark.parametrize("arr, expected", [
    ([5, 2, 3, 4, 1], [1, 2, 2, 3, 3, 4, 4, 5]),
    ([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854], [-20, 30]),
    ([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470], [-520, -470, -20, 30]),
    ([5, 4, 3, 2], [2, 3, 3, 4, 4, 5])
])
def test_closest_numbers(arr, expected):
    output = closest_numbers(arr)
    assert output == expected
