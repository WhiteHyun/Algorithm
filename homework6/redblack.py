from init import *


class RedBlack(Tree):
    """
    레드블랙트리 알고리즘입니다.
    """

    def insert(self, key: int) -> None:
        """
        key값을 레드블랙트리 개념에 따라 데이터를 삽입하는 메서드입니다.
        :param key: 삽입할 데이터
        :return:
        """
        x = p = g = gg = self.head
        while x != self.z:
            gg, g, p = g, p, x
            if x.key == key:
                return
            elif x.key > key:
                x = x.left
            else:
                x = x.right
            if x.left.color == RED and x.right.color == RED:
                self.__split(x, p, g, gg, key)
        x = node(key, self.z, self.z, color=RED)
        if p.key > key:
            p.left = x
        else:
            p.right = x
        self.__split(x, p, g, gg, key)
        if self.head.right.color == RED:
            self.head.right.color = BLACK

    def __split(self, x: node, p: node, g: node, gg: node, key: int) -> None:
        """
        데이터 삽입 후 완전한 레드블랙트리로 만들어주는 작업을 수행합니다.
        :param x: 현재 가리키고 있는 노드
        :param p: x의 부모노드
        :param g: p의 부모노드
        :param gg: g의 부모노드
        :param key: 삽입할 데이터
        :return:
        """
        x.color = RED
        x.left.color = x.right.color = BLACK
        if p.color == RED:
            g.color = RED
            if (g.key > key) != (p.key > key):
                p = self.__rotate(key, g)
            x = self.__rotate(key, gg)
            x.color = BLACK

    def __rotate(self, key: int, y: node) -> node:
        """
        레드블랙트리의 단일회전, 이중회전을 맡습니다.
        :param key: 삽입할 데이터
        :param y: 회전의 기준이 되는 노드
        :return node: 회전 후 기준이 되는 노드
        """

        # c: y의 자식 노드 gc: y의 손주노드
        c = gc = node

        """
        전달받은 파라미터를 가지고 자식과 손주노드를 구한 뒤, 회전시킵니다
        """
        if y.key > key:
            c = y.left
        else:
            c = y.right
        if c.key > key:
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

    def check(self, key_list: list, time: float) -> None:
        """
        레드 블랙 알고리즘이 정확하게 구현되었는지 체크하는 메서드입니다.
        """
        print("===================================")
        print(key_list)
        for key in sorted(key_list):
            x: node = self.head.right
            p: node = x
            while x != self.z:
                if x.key == key:
                    color = "black" if x.color == BLACK else "red"
                    print(f"key: {x.key}, parents: {p.key}, color: {color}")
                    break
                elif x.key > key:
                    p = x
                    x = x.left
                else:
                    p = x
                    x = x.right
        print(f'레드-블랙 트리 탐색(랜덤)의 실행 시간 (N= {len(key_list)}) : {time:.3f}')
        print('탐색 완료')
        print("===================================")
