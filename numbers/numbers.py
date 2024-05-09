from collections.abc import Iterable


from torch import nn

from pandas import Series

a = Series([1, 2, 3, 4, 5])

linear = nn.Linear(1, 1)


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterable of integers, return the sum of all even numbers in the iterable."""
    return sum(num for num in numbers if num % 2 == 0)


a = sum_even_numbers(
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]
)

a = (
    sum_even_numbers(
        [
            1,
            2,
            3,
        ]
    )
    + sum_even_numbers(
        [
            1,
            2,
            3,
        ]
    )
    + sum_even_numbers(
        [
            1,
            2,
            3,
        ]
    )
    + sum_even_numbers(
        [
            1,
            2,
            3,
        ]
    )
)
