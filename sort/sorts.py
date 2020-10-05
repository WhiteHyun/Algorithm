# 선택 정렬
def selection_sort(arr, size):
    for i in range(1, size):
        min_index = i
        for j in range(i+1, size+1):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 버블 정렬
def bubble_sort(arr, size):
    for i in range(size, 0, -1):
        for j in range(1, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 삽입 정렬
def insertion_sort(arr, size):
    for i in range(2, size+1):
        v, j = arr[i], i
        while j != 1 and arr[j-1] > v:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v
    return arr


# 쉘 정렬
def shell_sort(arr, size):
    h = 1
    while h < size:  # 첫 번째 h 값 계산
        h = 3*h+1
    while h > 0:    # h 값을 감소시키며 진행
        for i in range(h+1, size+1):
            v, j = arr[i], i
            while j > h and arr[j-h] > v:
                arr[j] = arr[j-h]
                j -= h
            arr[j] = v
        h //= 3
    return arr


# 퀵 정렬
def quick_sort(arr, l, r):
    if l < r:
        i = partition(arr, l, r)
        quick_sort(arr, l, i-1)
        quick_sort(arr, i+1, r)
    return arr


def partition(arr, l, r):
    v, i, j = arr[r], l-1, r
    while True:
        i += 1
        while arr[i] < v:
            i += 1

        j -= 1
        while j != 0 and arr[j] > v:
            j -= 1

        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[r] = arr[r], arr[i]
    return i


# 합병 정렬
def merge_sort(arr, tmp, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, tmp, l, mid)
        merge_sort(arr, tmp, mid+1, r)
        merge(arr, tmp, l, mid, r)
    return arr


def merge(arr, tmp, l, mid, r):
    for i in range(l, r+1):
        tmp[i] = arr[i]
    part1, part2, index = l, mid+1, l
    while part1 <= mid and part2 <= r:  # 서로 비교하며 merge
        if tmp[part1] <= tmp[part2]:
            arr[index] = tmp[part1]
            part1 += 1
        else:
            arr[index] = tmp[part2]
            part2 += 1
        index += 1
    # 앞 쪽(part1)이 남은경우 채워줌
    for i in range(mid-part1+1):
        arr[index+i] = tmp[part1+i]


# 힙 정렬
def heap_sort(arr, size):
    for i in range(size//2, 0, -1):
        heapify(arr, i, size)  # 최대 힙으로 만듦
    for i in range(size-1, 0, -1):
        # 최대 힙 상태에서 최상위 부모노드와 가장 밑 자식 노드와 교환
        arr[1], arr[i+1] = arr[i+1], arr[1]
        heapify(arr, 1, i)  # 최대 힙으로 다시 구성
    return arr


def heapify(arr, h, size):
    root = arr[h]   # root node
    c = 2*h  # child node index
    while c <= size:
        if c < size and arr[c] < arr[c+1]:  # 두 자식 노드 중에 큰 값을 가진 노드 인덱스로 이동
            c += 1
        if root >= arr[c]:  # 최대합이 된 경우
            break
        else:
            arr[c//2] = arr[c]  # 루트노드가 자식노드보다 작으므로 자식노드가 부모노드의 값으로 이동
        c *= 2
    arr[c//2] = root  # 옮길 루트노드 값을 최종 자식노드에 이동


# 계수 정렬
def counting_sort(arr, size, num_range):
    temp = arr.copy()
    count = [0] * (num_range+1)
    for i in arr[1:]:
        count[i] += 1
    for i in range(2, num_range+1):  # 중복 합 계산
        count[i] += count[i-1]
    for value in reversed(temp[1:]):
        arr[count[value]] = value
        count[value] -= 1
    return arr


# 기수 정렬
def radix_sort(arr, size, max_digit):
    queue = []
    for _ in range(10):
        queue.append([])
    for digit in range(1, max_digit+1):
        # digit에 따른 값을 인덱스로 하여 큐에 push
        for value in arr[1:]:
            index = find_digit(value, digit)
            enqueue(queue[index], value)
        # digit에 따라 큐에 들어간 값을 차례대로 pop하여 arr에 넣음
        index = 0
        for i in range(10):
            while len(queue[i]) != 0:
                index += 1
                arr[index] = dequeue(queue[i])
    return arr


def find_digit(num, digit):
    return (num % (10 ** digit)) // (10 ** (digit-1))


def enqueue(queue, data):
    queue.append(data)


def dequeue(queue):
    if len(queue) == 0:
        print('큐가 공백임')
        return -1
    else:
        data = queue.pop(0)
        return data


def check_sort(arr, n):
    is_sorted = True
    for i in range(1, n):
        if arr[i] > arr[i+1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")
