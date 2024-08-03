from hacker_hank.strong_password import minimum_number
from pytest import mark


@mark.parametrize("password, expected", [
    ("2bbbb", 2),
    ("2bb#A", 1),
    ("Ab1", 3)])
def test_strong_password(password, expected):
    output = minimum_number(len(password), password)
    assert output == expected
