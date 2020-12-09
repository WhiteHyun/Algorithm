import random


def shaker_sort(arr, n):
    r = n
    l = 1
    i = 1
    while l < r:
        if i % 2 == 1:
            for j in range(l+1, r+1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
            r -= 1
        else:
            for k in range(r, l, -1):
                if arr[k] < arr[k-1]:
                    arr[k], arr[k-1] = arr[k-1], arr[k]
            l += 1
        # print(f"{i}번째 패스 종료 후 arr = {arr}")
        i += 1
    return arr


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
        print(arr[:10])


if __name__ == "__main__":
    # a = []
    # a.append(-1)
    # for i in range(10):
    #     a.append(random.randint(1, 100))
    a = [-1, 6, 5, 4, 3, 2, 1]
    print(f"최초 배열 arr = {a}")
    shaker_sort(a, len(a)-1)
    check_sort(a, len(a)-1)
