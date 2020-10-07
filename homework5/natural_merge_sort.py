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
        new_run = []  # run 변수에 덮어 씌울 새로운 런 리스트 생성
        for i in range(0, len(run), 2):  # 런 합병 사이클 반복문
            temp_run = []   # 두 개의 런을 합병하여 new_run에 append할 임시 리스트
            part1 = run[i]
            if len(run)-1 >= i+1:
                part2 = run[i+1]
            else:
                part2 = []
            j = 0
            k = 0
            while len(part1) != j and len(part2) != k:
                if part1[j] < part2[k]:
                    temp_run.append(part1[j])
                    j += 1
                else:
                    temp_run.append(part2[k])
                    k += 1
            while len(part1) != j:
                temp_run.append(part1[j])
                j += 1
            while len(part2) != k:
                temp_run.append(part2[k])
                k += 1
            new_run.append(temp_run)
        run = new_run

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
    N = 100000
    # key = [-1, 6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
    key = list(range(1, N+1))
    random.shuffle(key)
    key.insert(0, -1)
    start_time = time.time()
    natural_merge_sort(key, len(key)-1)
    end_time = time.time()-start_time
    print('자연합병정렬(랜덤)의 실행 시간 (N= %d) : %f' % (N, end_time))
    check_sort(key, N)
