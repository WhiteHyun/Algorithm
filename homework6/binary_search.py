from init import *


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

    def check(self, key_list: list) -> None:
        """
        Tree의 추상메서드입니다.
        이진탐색트리에서는 check를 사용하지 않습니다.
        """
        return True
