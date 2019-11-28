from fizzbuzz import fizzbuzz


import pytest


@pytest.mark.parametrize(
    "number, expected", [(3, "Fizz"), (5, "Buzz"), (15, "Fizz Buzz"), (7, 7)]
)
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected
