from hacker_hank.running_time_of_algorithms import running_time_of_algorithms
from pytest import mark


@mark.parametrize("arr, expected", [
    ([2, 1, 3, 1, 2], 4)
])
def test_running_time_of_algorithms(arr, expected):
    output = running_time_of_algorithms(arr)
    assert output == expected
