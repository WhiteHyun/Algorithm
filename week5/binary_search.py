import random
import time


class node:
    def __init__(self, key=None):
        self.key = key


class Dict:
    def __init__(self):
        Dict.arr = []

    def search(self, search_key):
        n = len(self.arr)
        i = 0
        left = 0
        right = n-1
        while right >= left:
            i += 1
            mid = (left + right) // 2
            if self.arr[mid].key == search_key:
                return (i, mid)
            elif self.arr[mid].key > search_key:
                right = mid - 1
            else:
                left = mid + 1
        return None   # key 값이 존재하지 않음

    def insert(self, v):
        self.arr.append(node(v))


def quick_sort(arr, l, r):
    if r > l:
        i = partition(arr, l, r)
        quick_sort(arr, l, i-1)
        quick_sort(arr, i+1, r)


def partition(arr, l, r):
    v = arr[r]
    i = l - 1
    j = r
    while True:
        while True:
            i += 1
            if arr[i] >= v:
                break
        while True:
            j -= 1
            if j == 0 or arr[j] <= v:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[r] = arr[r], arr[i]
    return i


if __name__ == "__main__":
    key_num = 20000
    N = 20000
    key = list(range(1, key_num+1))
    s_key = list(range(1, N+1))
    random.shuffle(s_key)
    s_key.insert(0, -1)
    d = Dict()
    for i in range(key_num):
        d.insert(key[i])

    sum = 0
    start_time = time.time()
    quick_sort(s_key, 1, len(s_key)-1)
    s_key.pop(0)
    for i in range(N):
        temp, result = d.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            print("탐색오류")
        sum += temp
    end_time = time.time() - start_time
    avg = sum / N
    print('이진 탐색의 실행 시간 (key 개수 = %d, 찾는 key 개수 = %d) : %0.3f' %
          (key_num, N, end_time))
    print('탐색 완료')
    print(f'탐색횟수: {sum}')
    print(f'평균: {avg}')
