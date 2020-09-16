# import random
# import time


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


# if __name__ == "__main__":
#     N = 100000
#     arr = [-1]
#     for i in range(N):
#         arr.append(random.randint(1, N))

#     start_time = time.time()
#     arr_sort = quick_sort(arr, 1, N)
#     end_time = time.time() - start_time
#     print("퀵 정렬의 실행 시간 ( N = %d) : %0.3f" % (N, end_time))
