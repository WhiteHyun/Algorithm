from init import *


class AVL(Tree):
    """
    AVL트리 알고리즘입니다.
    """

    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0

    def search(self, searchKey):
        x = self.node
        while x is not None:
            if x.key == searchKey:
                return searchKey
            if x.key > searchKey:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, key):
        x = self.node
        if x is None:
            self.node = node(key, None, None)
            self.node.left = AVL()
            self.node.right = AVL()

        elif x.key > key:
            self.node.left.insert(key)

        else:
            self.node.right.insert(key)

        self.checkBalance()

    def checkBalance(self):
        self.updateHeight(False)
        self.updateBalance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotateLeft()
                self.rotateRight()

            else:
                if self.node.right.balance > 0:
                    self.node.right.rotateRight()
                self.rotateLeft()

            self.updateHeight()
            self.updateBalance()

    def rotateRight(self):
        g = self.node
        p = g.left.node
        x = p.right.node

        self.node = p
        p.right.node = g
        g.left.node = x

    def rotateLeft(self):
        g = self.node
        p = g.right.node
        x = p.left.node

        self.node = p
        p.left.node = g
        g.right.node = x

    def updateHeight(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateHeight()
                if self.node.right is not None:
                    self.node.right.updateHeight()
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1

        else:
            self.height = 0

    def updateBalance(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateBalance()
                if self.node.right is not None:
                    self.node.right.updateBalance()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check(self, key_list: list, time: float) -> None:
        """
        AVL 알고리즘이 정확하게 구현되었는지 체크하는 메서드입니다.
        """
        print("===================================")
        print(key_list)
        for key in sorted(key_list):
            x = p = self.node
            while x is not None:
                if x.key == key:
                    break
                if x.key > key:
                    p = x
                    x = x.left.node
                else:
                    p = x
                    x = x.right.node

            print(f'key: {x.key}, parent: {p.key}')
        print(f"AVL 트리 탐색(랜덤)의 실행 시간 (N = {len(key_list)}): {time:.3f}")
        print("탐색 완료")
        print("===================================")
