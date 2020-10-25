class Node:
    """
    탐색트리에 사용되는 노드 클래스입니다.

    Attributes:
        key (int): 노드의 탐색값입니다.
        left (Node): 이진 트리로 연결되며 자신의 왼쪽 자식노드를 가리킵니다.
        right (Node): 이진 트리로 연결되며 자신의 오른쪽 자식노드를 가리킵니다.
        bits (str): key값에 따른 이진수를 문자열입니다.
    """

    def __init__(self, key, left=None, right=None):
        """
        노드를 초기화 해주는 함수입니다.


        Args:
            key (int): 노드의 데이터로 들어갈 값
            left (node): 자신의 자식노드 중 왼쪽 노드
            right (node): 자신의 자식노드 중 오른쪽 노드


        Returns:
            None
        """
        temp_num = bin(key)[2:]
        self.__key = key
        self.__left = left
        self.__right = right
        self.__bits = "0" * (5 - len(temp_num)) + temp_num  # 5자리의 2진수로 수정

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def bits(self):
        return self.__bits

    @bits.setter
    def bits(self, bits):
        self.__bits = bits


class Tree():
    """
    노드가 들어갈 트리 알고리즘의 뼈대입니다.

    Attributes:
        head (Node): 트리에서 루트가 되는 속성입니다.
    """

    def __init__(self) -> None:
        self.head: Node = Node(0)
