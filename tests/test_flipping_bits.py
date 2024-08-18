from hacker_hank.flipping_bits import flipping_bits
from pytest import mark


@mark.parametrize("n, expected", [
    (9, 4294967286),
    (2147483647, 2147483648),
    (1, 4294967294),
    (0, 4294967295),
    (4, 4294967291),
    (123456, 4294843839)])
def test_flipping_bits(n, expected):
    output = flipping_bits(n)
    assert output == expected
