class Node:
    """
    탐색트리에 사용되는 노드 클래스입니다.
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
        self.__key = key
        self.__left = left
        self.__right = right

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
