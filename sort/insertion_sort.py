def insertion_sort(collection, verbose=False):
    """
    삽입정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> insertion_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> insertion_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> insertion_sort([])
        []
    """

    for i in range(1, len(collection)):
        if verbose:
            print(f"Rotation {i + 1}")

        temp = collection[i]

        for j in range(i - 1, -2, -1):
            if j < 0 or collection[j] <= temp:
                break
            collection[j + 1] = collection[j]
            if verbose:
                print(collection)

        collection[j + 1] = temp
        if verbose:
            print(collection)
    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(insertion_sort, True)
