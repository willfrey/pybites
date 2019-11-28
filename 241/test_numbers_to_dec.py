import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    "input_numbers, expected", [([0], 0), ([1], 1), ([1, 2], 12), ([0, 1], 1)]
)
def test_list_to_decimal(input_numbers, expected):
    assert list_to_decimal(input_numbers) == expected


def test_list_to_decimal_raises_with_empty_input():
    with pytest.raises(ValueError):
        list_to_decimal([])


@pytest.mark.parametrize("input_numbers", [[-1], [1, -1], [-1, 1]])
def test_list_to_decimal_raises_with_negative_numbers(input_numbers):
    with pytest.raises(ValueError):
        list_to_decimal(input_numbers)


@pytest.mark.parametrize("input_numbers", [[10], [1, 10], [10, 1], [0, 10]])
def test_list_to_decimal_raises_if_numbers_too_large(input_numbers):
    with pytest.raises(ValueError):
        list_to_decimal(input_numbers)


@pytest.mark.parametrize("input_numbers", [[1.2], [1.2, 1], [1, 1.2]])
def test_list_to_decimal_raises_if_numbers_are_not_int(input_numbers):
    with pytest.raises(TypeError):
        list_to_decimal(input_numbers)
