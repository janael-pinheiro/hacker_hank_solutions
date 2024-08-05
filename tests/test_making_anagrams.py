from hacker_hank.making_anagrams import making_anagrams
from pytest import mark


@mark.parametrize("s1, s2, expected", [
    ("abc", "amnop", 6),
    ("cde", "abc", 4),
    ("absdjkvuahdakejfnfauhdsaavasdlkj", "djfladfhiawasdkjvalskufhafablsdkashlahdfa", 19)])
def test_making_anagrams(s1, s2, expected):
    output = making_anagrams(s1, s2)
    assert output == expected
