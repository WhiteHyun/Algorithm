def bubble_sort(arr, N):
    i = index = 1
    length = N
    while index < length:
        if i % 2 == 1:  # 홀수일 경우
            for j in range(length-1, index+1, -1):
                if arr[j-1] > arr[j]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            index += 1
        else:  # 짝수일 경우
            for j in range(index, length-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            length -= 1
        print(f"i = {i}, {arr[1:]}")
        i += 1


if __name__ == "__main__":
    a = [-1, 0, 7, 5, 6, 4, 10, 9, 8, 1, 3, 2]
    N = len(a)
    print(f"a = {a[1:]}")
    bubble_sort(a, N)
