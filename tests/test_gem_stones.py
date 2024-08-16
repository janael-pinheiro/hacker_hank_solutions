from hacker_hank.gem_stones import gem_stones


def test_gem_stones():
    output = gem_stones(["abcdde", "baccd", "eeabg"])
    expected = 2
    assert output == expected
