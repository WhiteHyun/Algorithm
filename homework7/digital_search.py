from init import *


class DigitalSearch(Tree):
    """
    탐색 알고리즘 중 디지털 탐색 트리에 해당하는 클래스입니다.
    Tree를 상속받습니다. Tree에 대한 정보는 Tree.__doc__ 명령어를 사용해주세요.
    """

    def insert(self, key: int) -> int:
        """
        디지털 탐색 트리에서 노드를 넣는 함수입니다.

        Args:

            key (int): 노드의 key값을 넣기 위한 파라미터입니다. 

        Returns:
            0 : Success
            -1 : Fail
        """
        try:
            x: Node = self.head.right
            p_node: Node = self.head
            temp_node: Node = Node(key)
            i: int = 0
            while x is not None:
                p_node = x
                if temp_node.bits[i] == "1":
                    x = x.right
                else:
                    x = x.left
                i += 1
            if i == 0:
                p_node.right = temp_node
            else:
                if temp_node.bits[i-1] == "1":
                    p_node.right = temp_node
                else:
                    p_node.left = temp_node
        except:
            return -1  # FAIL
        return 0  # Success

    def search(self, search_key: int) -> int:
        """
        각 트리에 따른 탐색 함수입니다.

        Args:

            search_key (int): 트리 내에서 탐색할 key 값입니다.

        Returns:
            0: Success
            -1: Search Failed
            -2: Search Error
        """
        pass

    def check(self, key_list: list, time: float) -> None:
        """
        트리가 정확하게 구축되었는지 확인하여 출력해주는 메서드입니다.
        """
        pass


if __name__ == "__main__":
    d = DigitalSearch()
    keys = [1, 19, 5, 18, 3, 26, 9]
    for i in keys:
        d.insert(i)
