from functools import cmp_to_key

from hacker_hank.sorting_comparator import Player


def test_sorting_comparator():
    players = [Player("Smith", 20), Player("Jones", 15), Player("Jones", 20)]
    sorted_data = sorted(players, key=cmp_to_key(Player.comparator))
    expected = [Player("Jones", 20), Player("Smith", 20), Player("Jones", 15)]
    assert sorted_data[0].name == expected[0].name
    assert sorted_data[1].name == expected[1].name
    assert sorted_data[2].name == expected[2].name
    assert sorted_data[0].score == expected[0].score
    assert sorted_data[1].score == expected[1].score
    assert sorted_data[2].score == expected[2].score

