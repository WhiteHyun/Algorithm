# import random
# import time


def merge_sort(arr, l, r, b):
    if r > l:
        mid = (r + l) // 2
        merge_sort(arr, l, mid, b)
        merge_sort(arr, mid+1, r, b)
        for i in range(mid+1, l, -1):
            b[i-1] = arr[i-1]
        i -= 1
        for j in range(mid, r):
            b[r+mid-j] = arr[j+1]
        j += 1
        for k in range(l, r+1):
            if b[i] < b[j]:
                arr[k] = b[i]
                i += 1
            else:
                arr[k] = b[j]
                j -= 1


def check_sort(arr, n):
    is_sorted = True
    for i in range(1, n):
        if a[i] > arr[i+1]:
            is_sorted = False
        if not is_sorted:
            break
    if is_sorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")


# if __name__ == "__main__":
    # N = 100000
    # a = []
    # a.append(None)
    # for i in range(N):
    #     a.append(random.randint(1, N))
    # b = a.copy()
    # start_time = time.time()
    # merge_sort(a, 1, N, b)
    # end_time = time.time() - start_time
    # print(f"합병 정렬의 실행 시간 (N = {N} : {end_time}")
    # check_sort(a, N)
    # print(a)
