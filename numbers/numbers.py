from collections.abc import Iterable


from torch import nn

from pandas import Series

from numpy import arange
import numpy as np
import pandas as pd

k = pd.Series([1, 2, 3, 4, 5])


from numbers.util import func1, func2

a = np.array([1, 2, 3, 4, 5])

a = arange(10)

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
