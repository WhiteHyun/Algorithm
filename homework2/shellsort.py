def shell_sort(arr, n):
    h = 1
    while h < n:
        h *= 3
        h += 1
    while h > 0:
        for i in range(h+1, n+1):
            arr[0] = arr[i]
            j = i
            while(j > h and arr[j-h] > arr[0]):
                arr[j] = arr[j-h]
                j -= h
            arr[j] = arr[0]
        h //= 3
    return arr
# if __name__ == "__main__":
    # arr = [None, 3, 14, 12, 4, 10, 13, 15, 5, 2, 7, 9, 6, 8, 11, 1]
    # print(shell_sort(arr, len(arr)-1))

    # N = 20000
    # arr = []
    # for i in range(N):
    #     arr.append(random.randint(1, N))
    # arr.sort()
    # arr.reverse()

    # start_time = time.time()
    # arr_sort = shell_sort(arr, len(arr) - 1)
    # end_time = time.time() - start_time
    # print("쉘 정렬의 실행 시간 ( N = %d) : %0.3f" % (N, end_time))
