import random
import time


class node:
    def __init__(self, key=None):
        self.key = key


class Dict:
    def __init__(self):
        Dict.arr = []

    def search(self, search_key):
        i = 0
        n = len(self.arr)
        while i < n and self.arr[i].key != search_key:
            i += 1
        if i == n:
            return -1
        else:
            return i

    def insert(self, v):
        self.arr.append(node(v))


if __name__ == "__main__":
    key_num = 2000
    search_key_num = 2000
    key = list(range(1, key_num+1))
    s_key = list(range(1, search_key_num+1))
    random.shuffle(key)
    d = Dict()
    for i in range(key_num):
        d.insert(key[i])

    sum = 0
    start_time = time.time()
    for i in range(search_key_num):
        result = d.search(s_key[i])
        if result == -1 or key[result] != s_key[i]:
            print("탐색오류")
            result = key_num+1
        else:
            result += 1
        sum += result
    end_time = time.time() - start_time
    avg = sum / search_key_num

    print('순차 탐색의 실행 시간 (key 개수 = %d, search_key 개수 = %d) : %0.3f' %
          (key_num, search_key_num, end_time))
    print('탐색 완료')
    print(f'탐색횟수: {sum}')
    print(f'평균: {avg}')
