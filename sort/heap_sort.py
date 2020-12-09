
if __name__ == "__main__" or __name__ == "heap_sort":
    from common.util import *
else:
    from .common.util import *


def max_heapify(collection, root, heap_size):
    """최대 힙으로 만들어준다.
    서브트리가 최대힙이라 가정했을 때
    상향식 접근법이기 때문에 서브 트리를 히프화 해야한다.

    Args:
        collection (list): 부분적인 히프화 트리
        root (int): 루트 노드로 사용할 노드 인덱스
        heap_size (int): 히프화를 적용하기 위한 힙의 크기

    Returns:
        list: 히프화된 리스트

    Example:
        >>> max_heapify([3, 2, 5, 6, 8], 0, 3)
        [5, 2, 3, 6, 8]
        >>> max_heapify([3, 2, 5, 6, 8], 1, 5)
        [3, 8, 5, 6, 2]
        >>> max_heapify([3, 5, 8, 4, 2, 1, 6], 0, 7)
        [8, 5, 6, 4, 2, 1, 3]
        >>> max_heapify([2, 4, 7, 0, 1, 3, 8], 0, 6)
        [7, 4, 3, 0, 1, 2, 8]
    """

    left = (root << 1) + 1
    right = (root << 1) + 2

    bigger_one = root

    # Beware that the bigger_one will could be updated for two times.
    if left < heap_size and collection[left] > collection[bigger_one]:
        bigger_one = left

    if right < heap_size and collection[right] > collection[bigger_one]:
        bigger_one = right

    if bigger_one == root:
        return collection
    else:
        swap(collection, bigger_one, root)
        return max_heapify(collection, bigger_one, heap_size)


def heap_sort(collection, verbose=False):
    """
    힙 정렬 알고리즘

    Args:
        collection (list): 유저로부터 입력받은 정렬하기 전 리스트
        verbose (bool): 과정들을 출력하기 위한 flag

    Returns:
        list: 정렬된 리스트

    Example:
        >>> heap_sort([3, 1, 7, 0, 4, 8, 2])
        [0, 1, 2, 3, 4, 7, 8]
        >>> heap_sort([-91, -123, -1])
        [-123, -91, -1]
        >>> heap_sort([])
        []
    """

    size = len(collection)
    last_subtree_root = (size >> 1) - 1

    # 1. Build max heap.
    if verbose:
        print("1. Build max heap:")

    for i in range(last_subtree_root, -1, -1):
        max_heapify(collection, i, size)
        if verbose:
            print(collection)

    # 2. Send root to the end of the list.
    if verbose:
        print("2. Pick from root:")

    for i in range(size - 1, 0, -1):
        swap(collection, 0, i)
        if verbose:
            print(collection)

        max_heapify(collection, 0, i)
        if verbose:
            print(collection)

    return collection


if __name__ == "__main__":
    from common.invoker import from_input
    from_input(heap_sort, True)
