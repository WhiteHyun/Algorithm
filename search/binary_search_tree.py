import random
import time


class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Dict:
    x = p = node
    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            elif x.key > search_key:
                # print(f"{x.key} ==> ", end="")
                x = x.left
            else:
                # print(f"{x.key} ==> ", end="")
                x = x.right
        return -1

    def insert(self, v):
        x = self.head.right  # = z
        p = self.head
        while x != self.z:
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(v, self.z, self.z)

        if p.key > v:
            p.left = x
        else:
            p.right = x


if __name__ == "__main__":
    N = 20000
    # a = [2, 1, 7, 8, 6, 3, 5, 4]
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    random.shuffle(key)
    # key.sort(reverse=True)
    d = Dict()
    for i in key:
        d.insert(i)
    start_time = time.time()
    for i in s_key:
        result = d.search(i)
        if result == -1 or result != i:
            print('탐색 오류')
    end_time = time.time()-start_time
    print('이진 트리 탐색(랜덤)의 실행 시간 (N= %d) : %0.3f' % (N, end_time))
    print('탐색 완료')
