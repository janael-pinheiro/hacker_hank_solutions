from hacker_hank.ice_cream_parlor import ice_cream_parlor
from pytest import mark


@mark.parametrize("m, arr, expected", [
    (6, [1, 3, 4, 5, 6], [1, 4]),
    (4, [1, 4, 5, 3, 2], [1, 4]),
    (4, [2, 2, 4, 3], [1, 2])
])
def test_ice_cream_parlor(m, arr, expected):
    output = ice_cream_parlor(m, arr)
    assert output == expected
