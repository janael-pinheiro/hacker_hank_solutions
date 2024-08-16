from hacker_hank.funny_string import is_funny_string


def test_is_funny_string():
    input_string = "lmnop"
    expected_output = "Funny"
    real_output = is_funny_string(input_string)
    assert expected_output == real_output
