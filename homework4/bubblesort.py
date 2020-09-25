def bubble_sort(arr, n):
    for i in range(n, 0, -1):
        for j in range(1, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
