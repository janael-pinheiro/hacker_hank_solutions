from hacker_hank.strange_counter import strange_counter
from pytest import mark


@mark.parametrize("t, expected", [(1000, 534), (4, 6), (10, 12), (1, 3), (15, 7), (9, 1)])
def test_strange_counter(t, expected):
    output = strange_counter(t)
    expected = expected
    assert output == expected
