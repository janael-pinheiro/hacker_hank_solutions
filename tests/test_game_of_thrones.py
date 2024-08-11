from hacker_hank.game_of_thrones import game_of_thrones
from pytest import mark


@mark.parametrize("s,expected", [
    ("aabbccdd", "YES"),
    ("aaabbbb", "YES"),
    ("cdefghmnopqrstuvw", "NO")])
def test_game_of_thrones(s, expected):
    output = game_of_thrones(s)
    assert output == expected
