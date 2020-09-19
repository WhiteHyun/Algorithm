M = 30


def insertion_sort(arr, l, r):
    for i in range(l+1, r+1):
        v, j = arr[i], i
        while j > 1 and arr[j-1] > v:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = v


def quick_sort(arr, l, r):
    if r-l <= M:
        insertion_sort(arr, l, r)
    else:
        v, i, j = arr[r], l-1, r
        while True:
            i += 1
            while arr[i] < v:
                i += 1
            j -= 1
            while arr[j] > v:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[r] = arr[r], arr[i]
        quick_sort(arr, l, i-1)
        quick_sort(arr, i+1, r)
