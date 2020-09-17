def selection_sort(arr, n):
    for i in range(1, n):
        minimum = i
        for j in range(i + 1, n + 1):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr
