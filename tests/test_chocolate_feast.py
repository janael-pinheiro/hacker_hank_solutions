from hacker_hank.chocolate_feast import chocolate_feast
from pytest import mark


@mark.parametrize("input_value,expected", [
    ((6, 2, 2), 5),
    ((10, 2, 5), 6),
    ((12, 4, 4), 3),
    ((7, 3, 2), 3),
    ((16809, 123, 11668), 136),
    ((75807, 357, 21088), 212),
    ((43203, 60, 5), 899)
    ])
def test_chocolate_feast(input_value, expected):
    n, c, m = input_value
    output = chocolate_feast(n, c, m)
    assert output == expected
