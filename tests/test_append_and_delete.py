from hacker_hank.append_and_delete import append_and_delete
from pytest import mark


@mark.parametrize("s, t, k, expected", [
    ("abc", "def", 6, "Yes"),
    ("hackerhappy", "hackerrank", 9, "Yes"),
    ("aba", "aba", 7, "Yes"),
    ("ashley", "ash", 2, "No"),
    ("ashl", "ash", 3, "Yes"),
    ("aaaaaaaaaa", "aaaaa", 7, "Yes"),
    ("zzzzz", "zzzzzzz", 4, "Yes"),
    ("y", "yu", 2, "No"),
    ("asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv", 20, "Yes")])
def test_append_and_delete(s, t, k, expected):
    output = append_and_delete(s, t, k)
    assert output == expected
