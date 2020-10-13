from abc import ABCMeta, abstractmethod


RED = True
BLACK = False
FAIL = -1


class node:
    def __init__(self, key: int, left, right, color: bool = BLACK) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.color = color


class Tree(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.z = node(0, left=node, right=node)
        self.z.left = self.z.right = self.z
        self.head = node(0, left=self.z, right=self.z)

    def search(self, search_key) -> int:
        x: node = self.head.right
        while x != self.z:
            if x.key == search_key:
                return x.key
            elif x.key > search_key:
                x = x.left
            else:
                x = x.right
        return FAIL

    @abstractmethod
    def insert(self, key: int) -> None:
        """
        각 트리에 따른 데이터(key)를 넣는 메서드입니다.
        """
        pass

    @abstractmethod
    def check(self, key_list: list) -> None:
        """
        트리가 정확하게 구축되었는지 확인하여 출력해주는 메서드입니다.
        """
        pass
