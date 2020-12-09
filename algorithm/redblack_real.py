black = 0
red = 1

class node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color = color
        self.key = key
        self.right = right
        self.left = left

class Dict():
    x = p = q = gg = node
    z = node(color = black, key = 0, left = 0, right = 0)
    z.left = z
    z.right = z
    head = node(color = black, key = 0, left = 0, right = z)

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

    def insert(self, v):
        x = p = g = self.head
        while x != self.z:
            gg = g
            g = p
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right

            if x.left.color and x.right.color:
                self.split(x, p, g, gg, v)
        
        x = node(color = red, key = v, left = self.z, right = self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x
        self.split(x, p, g, gg, v)
        self.head.right.color = black

    def split(self, x, p, g, gg, v):
        x.color = red
        x.left.color = black
        x.right.color = black
        
        if p.color:
            g.color = red
            if (g.key > v) != (p.key > v):
                p = self.rotate(v, g)
            x = self.rotate(v, gg)
            x.color = black

    def rotate(self, v, y):
        gc = c = node
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

        if y.key > v:
            y.left = gc
        else:
            y.right = gc
        return gc


import random, time

def test(iNum):
    N = iNum
    key = list(range(1, N + 1))
    s_key = list(range(1, N + 1))

    random.shuffle(key)

    d = Dict()
    for i in range(0, N):
        d.insert(key[i])
    start_time = time.time()
    for i in range(N):
        result = d.search(s_key[i])
        if result == -1 or result != s_key[i]:
            print("탐색 오류")
    end_time = time.time() - start_time
    print("red-black Tree의 탐색 실행 시간(N = %d) : %0.3f"%(N, end_time))
    print("탐색완료")
        
test(10000)
test(20000)
test(30000)