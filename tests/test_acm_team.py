from hacker_hank.acm_team import acm_team
from pytest import mark


@mark.parametrize("topics, expected",
                  [(['10101', '11110', '00010'], (5, 1)),
                   (['10101', '11100', '11010', '00101'], (5, 2))
                   ])
def test_acm_team(topics, expected):
    output = acm_team(topics)
    assert output == expected
