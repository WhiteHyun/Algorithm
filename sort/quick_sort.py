
if __name__ == "__main__" or __name__ == "quick_sort":
    from common.util import *
else:
    from .common.util import *


def partition(collection: list, left: int, right: int) -> int:
    """Make left partition le pivot, right partition ge pivot.
    The pivot is selected by picking mid-index.

    Args:
        collection (list): Whole data.
        left (int): Index of start of left partition.
        right (int): Index of end of right partition.

    Returns:
        int: Index of the pivot.

    Example:
        >>> partition([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 6)
        5
    """

    # mid 인덱스를 리스트 오른쪽 인덱스에 둔다.
    mid = (left + right) // 2
    swap(collection, mid, right)

    pivot = collection[right]
    i = left - 1

    for j in range(left, right):
        if collection[j] < pivot:
            i += 1
            swap(collection, i, j)

    swap(collection, i + 1, right)

    return i + 1


def quick_sort(collection, verbose=False):
    """
    퀵 정렬 알고리즘
    재귀적 호출이 아닌 stack을 사용하여 구현되었음

    Args:
        collection (list): 유저로부터 입력받은 정렬 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> quick_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> quick_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> quick_sort([])
        []
    """

    stack = list()

    stack.append(0)  # l
    stack.append(len(collection) - 1)  # r

    while len(stack) > 0:
        r = stack.pop()
        l = stack.pop()

        # subarray의 크기가 1 또는 0인 경우 partition으로 나눌 필요 없음
        if l >= r:
            continue

        if verbose:
            print(f"{'     '*len(stack)}Partition {collection[l:r+1]}", end="")
        p = partition(collection, l, r)
        if verbose:
            print(f", pivot: {collection[p]}")

        # Elements on left
        if l < p-1:
            stack.append(l)
            stack.append(p - 1)

        # Elements on right
        if p + 1 < r:
            stack.append(p + 1)
            stack.append(r)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(quick_sort, True)
