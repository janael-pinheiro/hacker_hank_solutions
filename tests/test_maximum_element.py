from hacker_hank.maximum_element import get_max
from pytest import mark


@mark.parametrize("operations, expected", [
    (["1 97", "2", "1 20", "2", "1 26", "1 20", "2", "3", "1 91", "3"], [26, 91]),
    (["1 12", "2", "1 18", "2", "1 9", "1 75", "1 20", "1 49", "1 26", "3", "3", "3", "2", "3", "1 9", "3", "3", "3"], [75, 75, 75, 75, 75, 75, 75])
])
def test_get_max(operations, expected):
    output = get_max(operations)
    assert output == expected
