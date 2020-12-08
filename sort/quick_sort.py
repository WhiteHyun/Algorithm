
if __name__ == "__main__" or __name__ == "quick_sort":
    from common.util import *
else:
    from .common.util import *


def partition(collection: list, left: int, right: int) -> int:
    """pivot값은 가장 오른쪽으로 설정 

    Args:
        collection (list): 전체 데이터
        left (int): 파티션의 왼쪽 시작 인덱스
        right (int): 파티션의 오른쪽 끝 인덱스

    Returns:
        int: 피봇 인덱스

    Example:
        >>> partition([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 6)
        5
    """

    pivot = collection[right]
    i = left
    j = right - 1
    while True:
        while collection[i] < pivot:
            i += 1
        while collection[j] > pivot:
            j -= 1

        if i >= j:
            break

        swap(collection, i, j)

    swap(collection, i, right)

    return i


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
            print(f"{'    '*len(stack)}Partition {collection[l:r+1]}", end="")
        p = partition(collection, l, r)
        if verbose:
            print(f", pivot: {collection[p]}")
        print(f"{'    '*len(stack)}Sorted {collection}")

        # Elements on right
        if p + 1 < r:
            stack.append(p + 1)
            stack.append(r)

        # Elements on left
        if l < p - 1:
            stack.append(l)
            stack.append(p - 1)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(quick_sort, True)
