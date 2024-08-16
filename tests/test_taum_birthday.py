from hacker_hank.taum_birthday import taum_birthday
from pytest import mark


@mark.parametrize("input_data,expected", [
    ((3, 5, 3, 4, 1), 29),
    ((10, 10, 1, 1, 1), 20),
    ((5, 9, 2, 3, 4), 37),
    ((3, 3, 1, 9, 2), 12),
    ((3, 6, 9, 1, 1), 12)
])
def test_taum_birthday(input_data, expected):
    b, w, bc, wc, z = input_data
    output = taum_birthday(b, w, bc, wc, z)
    assert output == expected
