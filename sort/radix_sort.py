if __name__ == "__main__" or __name__ == "radix_sort":
    from common.util import *
else:
    from .common.util import *


def radix_sort(collection, verbose=False):
    """
    기수정렬 알고리즘
    자리수를 맞추어 입력하여야 한다.

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> radix_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> radix_sort([81, 12, 93, 23, 35, 46, 26, 67])
        [12, 23, 26, 35, 46, 67, 81, 93]

        >>> radix_sort([])
        []
    """
    from collections import deque

    if verbose:
        print(collection)
    size = get_digit(max(collection))

    # 숫자는 0~9, 10가지로 구성되어있음
    queue = [deque() for _ in range(10)]

    for digit_pos in range(size):
        # 자리수에 따라 queue를 이용하여 정렬
        for number in collection:
            digit_index = get_digit(number, digit_pos)
            queue[digit_index].append(number)

        # queue의 값을 collection으로 이동시켜 저장
        p = 0
        for i in range(10):
            while queue[i]:
                collection[p] = queue[i].popleft()
                p += 1

        if verbose:
            print(f"Rotation {digit_pos + 1} {collection}")

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(radix_sort, True)
