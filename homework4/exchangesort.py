# exchange_sort(a[], n)
#     for (i ← 1; i < n; i ← i + 1) do {
#         for (j ← i + 1; j ≤ n; j ← j + 1) do {
#             if (a[i] < a[j]) do then change
#         }
#     }
# end exchange_sort()
import random
import time


def exchange_sort(arr, n):
    for i in range(1, n):
        for j in range(i+1, n+1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        # print(f"{i}번째 패스 종료 후 arr = {arr}")
    return arr


if __name__ == "__main__":
    arr = [-1]
    data = 10
    for i in range(data):
        arr.append(random.randint(1, data))
    start_time = time.time()
    arr_sort = exchange_sort(arr, len(arr) - 1)
    end_time = time.time() - start_time
    print("교환 정렬의 실행 시간 ( data = %d) : %0.3f" % (data, end_time))
