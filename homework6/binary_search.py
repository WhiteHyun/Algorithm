from init import *

import random
import time


class BinarySearch(Tree):

    def insert(self, key: int) -> None:
        x: node = self.head.right
        p: node = self.head
        while x != self.z:
            p = x
            if x.key == key:
                return None
            elif x.key > key:
                x = x.left
            else:
                x = x.right
        x = node(key, self.z, self.z)

        if p.key > key:
            p.left = x
        else:
            p.right = x

    def check(self, search_list: list) -> None:
        """
        Tree의 추상메서드입니다.
        이진탐색트리에서는 check를 사용하지 않습니다.
        """
        return True


if __name__ == "__main__":
    N = 20000
    # key = [2, 1, 7, 8, 6, 3, 5, 4]
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    random.shuffle(key)
    # key.sort(reverse=True)
    d = BinarySearch()
    for i in key:
        d.insert(i)
    start_time = time.time()
    for i in s_key:
        result = d.search(i)
        if result == -1 or result != i:
            print('탐색 오류')
    end_time = time.time()-start_time
    print(f'이진 트리 탐색(랜덤)의 실행 시간 (N= {N}) : {end_time:.3f}')
    print('탐색 완료')
