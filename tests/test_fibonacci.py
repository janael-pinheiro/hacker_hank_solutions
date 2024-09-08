from hacker_hank.fibonacci_numbers import fibonacci
from pytest import mark


@mark.parametrize("n, expected", [
    (3, 2)
])
def test_fibonacci(n, expected):
    output = fibonacci(n)
    assert output == expected

