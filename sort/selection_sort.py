def selection_sort(collection, verbose=False):
    """
    선택정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> selection_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> selection_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> selection_sort([])
        []
    """

    for i in range(len(collection) - 1):
        if verbose:
            print(f"Rotation {i + 1}")

        min_index = i

        # Find the index of the minimum item.
        for j in range(i, len(collection)):
            if collection[min_index] > collection[j]:
                min_index = j

        # Swap if found something smaller than it has.
        if min_index != i:
            collection[min_index], collection[i] = collection[i], collection[min_index]
            if verbose:
                print(collection)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(selection_sort, True)
