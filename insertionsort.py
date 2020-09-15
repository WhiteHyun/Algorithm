def insertion_sort(arr, n):
    for i in range(2, n+1):
        v, j = arr[i], i
        while arr[j-1] > v and j > 1:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v
    return arr
