class bitskey:
    def __init__(self, x):
        self.x = x

    def get(self):
        return self.x

    def __bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

    def print(self):
        for i in range(4, -1, -1):
            print(self.__bits(i, 1), end="")


def puts() -> bitskey:
    return bitskey(int(input("자연수 입력: ")))


d = puts()
d.print()
