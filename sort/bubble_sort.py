def bubble_sort(collection, verbose=False):
    """
    버블정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> bubble_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> bubble_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> bubble_sort([])
        []
    """

    for i in range(len(collection) - 1):
        if verbose:
            print(f"Rotation {i + 1}")

        for j in range(len(collection) - 1 - i):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] \
                    = collection[j + 1], collection[j]
            if verbose:
                print(collection)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(bubble_sort, True)
