def get_gap(number):
    """shell sort의 h값을 구한다.

    Args:
        number (int): 반올림할 수

    Returns:
        int: 홀수로 반올림된 수

    Example:
        >>> get_gap(3)
        1
        >>> get_gap(5)
        4
        >>> get_gap(15)
        13
    """
    gap = 1
    while gap < number:
        gap = gap * 3 + 1
    return (gap - 1) // 3


def subarray_insertion_sort(collection, first, last, gap, verbose=False):
    """gap에 따른 삽입 정렬

    Args:
        collection (list): 입력받은 정렬 리스트
        first (int): 정렬을 적용할 첫 번째 인덱스
        last (int): 정렬을 적용할 마지막 인덱스
        gap (int): 정렬할 요소 사이 간격
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬 적용한 collection

    Example:
        >>> subarray_insertion_sort([7, 345, 6, 5, 128, 4, 3, 243], 1, 7, 3)
        [7, 128, 6, 5, 243, 4, 3, 345]
    """

    if verbose:
        print(f"first: {first} last: {last} gap: {gap}")
        print(collection)

    rotation = 1

    for i in range(first + gap, last + 1, gap):
        if verbose:
            print(f"    Rotation {rotation}")

        temp = collection[i]

        for j in range(i - gap, first - gap - 1, -gap):
            if j < 0 or collection[j] <= temp:
                break

            collection[j + gap] = collection[j]
            if verbose:
                print(collection)

        collection[j + gap] = temp

        if verbose:
            print(collection)

        rotation += 1

    return collection


def shell_sort(collection, verbose=False):
    """
    쉘 정렬 알고리즘
    gap 값에 따른 삽입정렬로 삽입 정렬의 변형이다.

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> shell_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> shell_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> shell_sort([])
        []
    """
    #1, 4, 13, 40
    size = len(collection)
    gap = get_gap(size)
    rotation = 1

    while gap > 0:
        if verbose:
            print(f"Rotation {rotation}")

        # Number of subarrays: gap
        for i in range(gap + 1):
            if i + gap >= size:
                break
            subarray_insertion_sort(collection, i, size - 1, gap, verbose)

        gap = (gap - 1) // 3
        rotation += 1
    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(shell_sort, True)
