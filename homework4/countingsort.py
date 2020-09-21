import time
import random


def counting_sort(arr, n, m):
    # n = 길이, m = key 값의 개수
    count = [0] * (m+1)
    b = [0] * (n+1)
    try:
        for i in range(1, n+1):  # 원소의 개수를 세어 count에 저장
            count[arr[i]] += 1
        for j in range(2, m+1):  # 중복합 계산
            count[j] += count[j-1]
        for i in range(n, 0, -1):
            b[count[arr[i]]] = arr[i]  # arr의 원소를 b의 미리 계산된 위치로 이동
            count[arr[i]] -= 1  # count의 값을 하나 감소시킴
        for i in range(1, n+1):
            arr[i] = b[i]
    except:
        print(f"arr[i] = {arr[i]}, i = {i}, count[arr[i]] = {count[arr[i]]}")

# m = 1000, n = 100000일 때 구하기


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


if __name__ == "__main__":
    N = 100000
    M = 1000
    a = [None]
    for i in range(N):
        a.append(random.randint(1, M))
    print(len(a))
    start_time = time.time()
    counting_sort(a, N, M)
    end_time = time.time() - start_time
    print(f"계수 정렬의 실행 시간 (N = {N} : {end_time}")
    check_sort(a, N)
