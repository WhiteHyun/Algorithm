import random
import time

BLACK = False
RED = True


class node:
    def __init__(self, key: int = None, left=None, right=None, color: bool = BLACK):
        self.key = key
        self.left = left
        self.right = right
        self.color = color


class Dict:
    z = node(key=0, left=node, right=node, color=BLACK)
    z.left = z
    z.right = z
    head = node(key=0, left=z, right=z)

    def search(self, search_key):
        x = self.head.right

        while x != self.z:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left
            else:
                x = x.right
        return -1

    def insert(self, v: int):
        x = p = g = gg = self.head
        while x != self.z:
            gg, g, p = g, p, x
            if x.key == v:
                return
            elif x.key > v:
                x = x.left
            else:
                x = x.right
            if x.left.color == RED and x.right.color == RED:
                self.split(x, p, g, gg, v)
        x = node(v, self.z, self.z, color=RED)
        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        if self.head.right.color == RED:
            self.head.right.color = BLACK

    def split(self, x: node, p: node, g: node, gg: node, v: int):
        x.color = RED
        x.left.color, x.right.color = BLACK, BLACK
        if p.color == RED:
            g.color = RED
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = BLACK

    def rotate(self, v: int, y: node):
        # c: y의 자식 노드, gc: y의 손주 노드
        c = gc = node
        if y.key > v:
            c = y.left
        else:
            c = y.right
        if c.key > v:
            gc = c.left
            c.left = gc.right
            gc.right = c
        else:
            gc = c.right
            c.right = gc.left
            gc.left = c

        if y.left == c:
            y.left = gc
        elif y.right == c:
            y.right = gc
        return gc


if __name__ == "__main__":
    N = 20000
    key = list(range(1, N+1))
    s_key = list(range(1, N+1))
    random.shuffle(key)
    d = Dict()
    # key = [66, 78, 80, 25, 20, 61, 19, 30, 34, 32, 71]
    for i in key:
        d.insert(i)

    start_time = time.time()
    for i in s_key:
        result = d.search(i)
        if result == -1 or result != i:
            print('탐색 오류')
    end_time = time.time()-start_time

    print('레드-블랙 트리 탐색(랜덤)의 실행 시간 (N= %d) : %0.3f' % (N, end_time))
    print('탐색 완료')
