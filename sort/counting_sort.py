if __name__ == "__main__" or __name__ == "counting_sort":
    from common.util import *
else:
    from .common.util import *


def counting_sort(collection, verbose=False):
    """
    계수정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> counting_sort([6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6]

        >>> counting_sort([1, 2, 2, 1, 3, 4, 4, 1])
        [1, 1, 1, 2, 2, 3, 4, 4]

        >>> counting_sort([])
        []
    """
    max_number = max(collection)
    size = len(collection)
    count = [0] * max_number

    for i in collection:
        count[i-1] += 1

    # 중복합 계산
    for j in range(1, max_number):
        count[j] += count[j-1]

    if verbose:
        print(f"{collection}    {count}")

    # 리스트의 원소를 copy list의 미리 계산된 위치로 이동 후 count값 감소
    for i in copy_list(collection)[::-1]:
        collection[count[i-1]-1] = i
        count[i-1] -= 1
        if verbose:
            print(f"{collection}    {count}")

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(counting_sort, True)
