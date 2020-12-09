import time
import random


class Dict:
    def __init__(self):
        Dict.a = [-1] * M

    def search(self, v):
        x = self.hash(v)
        u = self.hash2(v)

        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]

            else:
                x = (x + u) % M

        return -1

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)

        while Dict.a[x] != -1:
            x = (x + u) % M
        Dict.a[x] = v

    def hash(self, v):
        return v % M

    def hash2(self, v):
        return 64 - (v % 64)

    def print(self):
        for i in range(M):
            if Dict.a[i] != -1:
                print('#', end='')

            else:
                print(' ', end='')

            if (i + 1) % 60 == 0:
                print()


if __name__ == "__main__":
    N = 10000
    M = 10391
    key = []
    s_key = []

    for i in range(N):
        r = random.randint(1, 3 * N)
        key.append(r)
        s_key.append(r)

    d = Dict()

    for i in range(N):
        d.insert(key[i])

    start_time = time.time()

    for i in range(N):
        result = d.search(s_key[i])

        if result == -1 or result != s_key[i]:
            print('Search Error!')

    end_time = time.time() - start_time

    print(f'Double Hashing Time (N = {N}, M = {M}) : {end_time:.3f}')
    print('Search Complete')
    # d.print()
