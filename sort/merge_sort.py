def merge(collection, left, middle, right, verbose=False, level=0):
    """두 개의 서브리스트를 합친다:
    collection[left:middle+1] 과 collection[middle+1:right+1].

    Args:
        collection (list): 두 정렬된 서브리스트를 가지고 있는 리스트.
        left (int): 왼쪽 서브리스트의 시작 인덱스.
        middle (int): 왼쪽 리스트의 끝 인덱스.
        right (int): 오른쪽 리스트의 끝 인덱스.
        verbose (bool): step을 보여주거나 보여주지 않는 flag값.
        level (int): 함수의 call이 얼마나 진행되었는지 깊이를 보여주는 레벨 값.

    Return:
        list: 두 서브리스트가 합병된 리스트
    """

    left_half = collection[left:middle+1]
    right_half = collection[middle+1:right+1]

    k = left
    l = 0
    r = 0

    # Copy items to collection in ascending order.
    while l < len(left_half) and r < len(right_half):
        if left_half[l] <= right_half[r]:
            collection[k] = left_half[l]
            l += 1
        else:
            collection[k] = right_half[r]
            r += 1
        k += 1
        if verbose:
            print(f"{'    '*level}{collection[left:k]}")

    # Copy remaining items in left half
    while l < len(left_half):
        collection[k] = left_half[l]
        k += 1
        l += 1
        if verbose:
            print(f"{'    '*level}{collection[left:k]}")

    # Copy remaining items in right half
    while r < len(right_half):
        collection[k] = right_half[r]
        k += 1
        r += 1
        if verbose:
            print(f"{'    '*level}{collection[left:k]}")

    if verbose:
        print(f"{'    '*level}Merged: {collection[left:right+1]}")

    return collection


def merge_sort_recursive(collection, left, right, verbose=False, level=0):
    """재귀적 방법으로 구현된 합병 정렬

        Args:
            collection (list): The collection to sort.
            left (int): Most left index of collection to sort.
            right (int): Most right index of collection to sort.
            verbose (bool): Print steps or not.
            level (int): Indent level. Used to distinguish call depth.

        Returns:
            list: The sorted collection.

        Example:
            >>> merge_sort_recursive([4, 7, 8, 2, 5], 0, 4, False)
            [2, 4, 5, 7, 8]
            >>> merge_sort_recursive([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 3, False)
            [6, 7, 8, 9, 5, 4, 3, 2, 1]
    """

    if left >= right:
        return collection

    middle = left + ((right - left) >> 1)

    if verbose:
        print(f"{'    '*level}1. Left: {collection[left:middle+1]}")
    merge_sort_recursive(collection, left, middle, verbose, level + 1)

    if verbose:
        print(f"{'    '*level}2. Right: {collection[middle+1:right+1]}")
    merge_sort_recursive(collection, middle + 1, right, verbose, level + 1)

    if verbose:
        print(
            f"{'    '*level}3. Merge: {collection[left:middle+1]} and {collection[middle+1:right+1]}")
    merge(collection, left, middle, right, verbose, level + 1)

    return collection


def merge_sort(collection, verbose=False):
    """
    합병 정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> merge_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> merge_sort([-154, -91, -27])
        [-154, -91, -27]

        >>> merge_sort([])
        []
    """

    merge_sort_recursive(collection, 0, len(collection) - 1, verbose, 0)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(merge_sort, True)
