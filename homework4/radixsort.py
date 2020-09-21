import random
import time


def radix_sort(arr, n, m, q):
    # m = digit 수, k = 1은 가장 작은 자리 수
    for k in range(1, m+1):
        for i in range(1, n+1):
            kd = digit(arr[i], k)
            enqueue(q[kd], arr[i])
        p = 0
        for i in range(10):
            while len(q[i]) != 0:
                p += 1
                arr[p] = dequeue(q[i])


def digit(num, k):
    for _ in range(k-1):
        num //= 10
    return num % 10


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
        print(f"arr[i] = {arr[i]}, arr[i+1] = {arr[i+1]}, i = {i}")


if __name__ == "__main__":
    M = 5
    N = 100000
    a = []
    a.append(-1)
    for i in range(N):
        a.append(random.randint(1, N-1))
    Q = []
    for i in range(10):
        Q.append([])
    start_time = time.time()
    radix_sort(a, N, M, Q)
    end_time = time.time() - start_time
    print(f"기수 정렬의 실행 시간 ( N = {N}) : {end_time}")
    check_sort(a, N)
