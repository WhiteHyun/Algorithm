
FAIL = -1


class Node():
    def __init__(self, key: int = 0, left=None, right=None) -> None:
        self.key = key
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self) -> None:
        self.head = Node()

    def search(self, key: int):
        if self.head.right is None:
            print("tree is empty")
            return
        p = self.head
        x = p.right
        while x is not None:
            p = x
            if x.key == key:
                return x.key
            elif x.key < key:
                x = x.right
                print("right", end=" ")
            else:
                x = x.left
                print("left", end=" ")
        return -1

    def insert(self, key: int):
        if self.head.right is None:
            self.head.right = Node(key)
        p = self.head
        x = self.head.right
        while x is not None:
            p = x
            if x.key < key:
                x = x.right
            else:
                x = x.left

        x = Node(key)
        if p.key < key:
            p.right = x
        else:
            p.left = x


if __name__ == "__main__":
    key = [2, 1, 7, 8, 6, 3, 5, 4]
    d = BinaryTree()
    for i in key:
        d.insert(i)
    while True:
        s_key = int(input("탐색키 입력: "))
        if s_key == 999:
            print("프로그램 종료")
            break
        result = d.search(s_key)
        if result == s_key:
            print("\n탐색 성공\n")
        else:
            print("\n탐색 실패\n")
