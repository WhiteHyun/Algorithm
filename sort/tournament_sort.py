import random
import time


def tournament_sort(arr, n):
    count = 1
    length = n
    b = []
    while length//2 != 0:
        count += 1
        length /= 2
    m = 2 ** (count+1)
    # b 할당부분
    for i in range(2**count):
        b.append(0)
    for i in range(2**count):
        if i < n:
            b.append(arr[i])
        else:
            b.append(0)

    for i in range(n-1, -1, -1):
        # 토너먼트
        for j in range(2**count-1, 0, -1):
            child1 = b[j*2]
            child2 = b[j*2+1]
            if child1 < child2:
                b[j] = child2
            else:
                b[j] = child1
        arr[i] = b[1]  # 값 추가
        # print(b)
        # 토너먼트 우승한 값을 0으로 초기화 하는 작업
        j = 1
        while j*2 < m:
            if b[j] == b[j*2]:
                j *= 2
            else:
                j = j*2+1
        b[j] = 0


if __name__ == "__main__":
    N = 5000
    # key = [4, 6, 7, 3, 5, 1, 2]
    key = list(range(1, N+1))
    # random.shuffle(key)
    key.sort(reverse=True)
    start_time = time.time()
    tournament_sort(key, len(key))
    end_time = time.time()-start_time
    print('토너먼트 정렬(역순정렬됨)의 실행 시간 (N= %d) : %0.3f' % (N, end_time))
