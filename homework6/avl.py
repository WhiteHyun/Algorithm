from init import *


class AVL(Tree):
    """
    AVL트리 알고리즘입니다.
    """

    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0

    def search(self, search_key: int) -> int:
        x = self.node
        while x is not None:
            if x.key == search_key:
                return search_key
            if x.key > search_key:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, key: int) -> None:
        x = self.node
        if x is None:
            self.node = node(key, left=None, right=None)
            self.node.left = AVL()
            self.node.right = AVL()

        elif x.key > key:
            self.node.left.insert(key)

        else:
            self.node.right.insert(key)

        self.__check_balance()

    def __check_balance(self) -> None:
        self.__update_height(False)
        self.__update_balance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.__rotate_left()
                self.__rotate_right()

            else:
                if self.node.right.balance > 0:
                    self.node.right.__rotate_right()
                self.__rotate_left()

            self.__update_height()
            self.__update_balance()

    def __rotate_right(self) -> None:
        g = self.node
        p = g.left.node
        x = p.right.node

        self.node = p
        p.right.node = g
        g.left.node = x

    def __rotate_left(self) -> None:
        g = self.node
        p = g.right.node
        x = p.left.node

        self.node = p
        p.left.node = g
        g.right.node = x

    def __update_height(self, recurse=True) -> None:
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.__update_height()
                if self.node.right is not None:
                    self.node.right.__update_height()
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1

        else:
            self.height = 0

    def __update_balance(self, recurse=True) -> None:
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.__update_balance()
                if self.node.right is not None:
                    self.node.right.__update_balance()
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
