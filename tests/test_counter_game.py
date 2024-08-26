from hacker_hank.counter_game import counter_game
from pytest import mark


@mark.parametrize("n, expected", [
    (1, "Richard"),
    (132, "Louise"),
    (6, "Richard"),
    (2, "Louise"),
    (1560834904, "Richard"),
    (1768820483, "Richard"),
    (1533726144, "Louise"),
    (1620434450, "Richard"),
    (1463674015, "Louise")
])
def test_counter_game(n, expected):
    output = counter_game(n)
    assert output == expected
