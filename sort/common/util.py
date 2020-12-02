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
