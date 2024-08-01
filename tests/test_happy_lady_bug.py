from hacker_hank.happy_lady_bug import happy_lady_bug
from pytest import mark


@mark.parametrize("input_data,expected", [
    ("RBY_YBR", "YES"),
    ("X_Y__X", "NO"),
    ("__", "YES"),
    ("B_RRBR", "YES"),
    ("AABBC", "NO"),
    ("AABBC_C", "YES"),
    ("DD__FQ_QQF", "YES"),
    ("AABCBC", "NO"),
    ("RRRR", "YES"),
    ("BBB_", "YES"),
    ("G", "NO"),
    ("RRGGBBXX", "YES"),
    ("_FWYSSENEDBO_KSEVUAB_WZ_GASASVEVS_O_NSVBYFNADE_WWVSBKAE_F_VAS_F_AAAEWBE_WEAEOAYV", "NO"),
    ("PHMWXXPWWXWWXHW", "NO"),
    ("KTXODXKXDXXDDOXX", "NO"),
    ("ZF__KSHMNOILMFIMFHFM_ZNIMLFHLNOLZNM", "NO"),
    ("IIIAA", "YES")])
def test_happy_lady_bug(input_data, expected):
    output = happy_lady_bug(input_data)
    assert output == expected

