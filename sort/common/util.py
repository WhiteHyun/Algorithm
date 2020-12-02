import time
import copy
import random


def average(collection: list) -> float:
    """리스트의 평균값을 구한다.

    Example:
        >>> average([3, 4, 5])
        4.0
    """
    return sum(collection) / len(collection)


def copy_list(origin):
    return copy.deepcopy(origin)


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


def get_digit(number, position=-1):
    """숫자의 자리수를, 또는 해당 위치의 값을 구한다.

    Example:
        >>> get_digit(15427)
        5

        >>> get_digit(15427, 2)
        4

        >>> get_digit(49)
        2

        >>> get_digit(49, 1)
        4
    """
    digit = 0
    if position == -1:
        while number != 0:
            number //= 10
            digit += 1
    else:
        digit = number % (10**(position+1))
        digit //= 10**(position)

    return digit
