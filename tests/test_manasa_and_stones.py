from hacker_hank.manasa_and_stones import stones

from pytest import mark


@mark.parametrize("n,a,b,expected", [
    (2, 1, 1, [1]),
    (100, 1, 1, [99]),
    (3, 2, 3, [4, 5, 6]),
    (3, 1, 2, [2, 3, 4]),
    (4, 10, 100, [30, 120, 210, 300])
])
def test_stones(n, a, b, expected):
    output = stones(n, a, b)
    assert expected == output
