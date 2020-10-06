import time
import random


def find_run(arr: list, n: int):
    ret_arr = []
    part_arr = [arr[1]]
    for i in range(2, n+1):
        if arr[i-1] < arr[i]:
            part_arr.append(arr[i])
        else:
            ret_arr.append(part_arr)
            part_arr = [arr[i]]
    ret_arr.append(part_arr)
    return ret_arr


def natural_merge_sort(arr: list, n: int):
    run = find_run(arr, n)  # 런을 구함
    while len(run) != 1:    # 런의 크기가 1이 될 때까지 반복
        # print(run)
        for i in range(len(run)//2):  # 런 합병 사이클 반복문
            part1 = run.pop(i)  # 두 런 중에 앞의 런만 pop하여 뒤의 런에 값 할당
            part2 = run[i]
            j = 0
            k = 0
            while len(part1) != j and len(part2) != k:
                if part1[j] < part2[k]:
                    part2.insert(k, part1[j])
                    j += 1
                    k += 1
                else:
                    k += 1
            while len(part1) != j:
                part2.append(part1[j])
                j += 1
    # 기존 array에 정렬 값 저장
    for i in range(1, n+1):
        arr[i] = run[0][i-1]
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


if __name__ == "__main__":
    N = 10000
    # key = [-1, 6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
    key = list(range(1, N+1))
    random.shuffle(key)
    key.insert(0, -1)
    start_time = time.time()
    natural_merge_sort(key, len(key)-1)
    end_time = time.time()-start_time
    print('자연합병정렬(랜덤)의 실행 시간 (N= %d) : %f' % (N, end_time))
    check_sort(key, N)
