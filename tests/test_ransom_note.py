from hacker_hank.ransom_note import check_magazine
from pytest import mark


@mark.parametrize("magazine, note, expected", [
    ("give me one grand today night", "give one grand today", "Yes\n"),
    ("two times three is not four", "two times two is four", "No\n"),
    ("ive got a lovely bunch of coconuts", "ive got some coconuts", "No\n")
])
def test_check_magazine(magazine, note, expected, capsys):
    check_magazine(magazine, note)
    captured = capsys.readouterr()
    assert captured.out == expected
