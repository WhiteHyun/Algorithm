from init import *

INTERNAL_NODE_VALUE = -1


class RadixSearchTrie(Tree):
    """
    탐색 알고리즘 중 기수 탐색 트라이에 해당하는 클래스입니다.
    Tree를 상속받습니다. Tree에 대한 정보는 Tree.__doc__ 명령어를 사용해주세요.
    """

    def insert(self, key: int) -> int:
        """
        기수 탐색 트라이에서 노드를 넣는 함수입니다.

        Args:

            key (int): 노드의 key값을 넣기 위한 파라미터입니다.

        Returns:
            0 : Success
            -1 : Fail
        """
        try:
            x: Node = self.head.right  # 비교노드
            p_node: Node = self.head    # 부모노드
            temp_node: Node = Node(key)  # Insert할 임시 노드
            h: int = 0  # 노드간 height 또는 비트의 인덱스
            # 값이 존재하지 않거나 내부노드인 경우만 반복하여 넣을 공간을 찾아감
            while x is not None and x.key == INTERNAL_NODE_VALUE:
                p_node = x
                if temp_node.bits[h] == "1":
                    x = x.right
                else:
                    x = x.left
                h += 1
            # 첫 번째 노드를 넣을 경우
            if h == 0 and x is None:
                p_node.right = temp_node
            # 단독으로 노드를 넣을 경우
            elif x is None:
                if p_node.right == x:
                    p_node.right = temp_node
                else:
                    p_node.left = temp_node
            # 존재하고있는 key값과 경쟁을 하는 경우
            else:
                # 먼저 내부노드를 설정하여 부모노드와 연결한다.
                internal_node = Node(INTERNAL_NODE_VALUE)
                if p_node.right == x:
                    p_node.right = internal_node
                else:
                    p_node.left = internal_node
                p_node = internal_node
                # 기존에 존재하던 노드와 넣을 노드간 비트 비교를 통해 내부노드를 따라 내려갈지 아닐지를 결정한다.
                while x.bits[h] == temp_node.bits[h]:
                    internal_node = Node(INTERNAL_NODE_VALUE)
                    if temp_node.bits[h] == "1":
                        p_node.right = internal_node
                    else:
                        p_node.left = internal_node
                    p_node = internal_node
                    h += 1
                # 경쟁이 끝났다면 각 비트에 따라 자식노드로 넣어준다
                if temp_node.bits[h] == "1":
                    p_node.right = temp_node
                    p_node.left = x
                else:
                    p_node.right = x
                    p_node.left = temp_node
        except:
            return -1  # FAIL
        return 0  # Success


if __name__ == "__main__":
    d = RadixSearchTrie()
    keys = [1, 19, 5, 18, 3, 26, 9]
    for i in keys:
        result = d.insert(i)
        if result == -1:
            print(f'오류! key = {i}')
