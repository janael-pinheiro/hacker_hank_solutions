from hacker_hank.big_sorting import big_sorting
from pytest import mark


@mark.parametrize("unsorted, expected", [
    (["1", "200", "150", "3"], ["1", "3", "150", "200"]),
    (["31415926535897932384626433832795", "1", "3", "10", "3", "5"], ["1", "3", "3", "5", "10", "31415926535897932384626433832795"]),
    (["1", "2", "100", "12303479849857341718340192371", "3084193741082937", "3084193741082938", "111", "200"], ["1", "2", "100", "111", "200", "3084193741082937", "3084193741082938", "12303479849857341718340192371"])
])
def test_big_sorting(unsorted, expected):
    output = big_sorting(unsorted)
    assert output == expected
