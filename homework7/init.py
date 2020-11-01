from abc import ABCMeta, abstractmethod

maxb = 5
ERROR = -2
FAIL = -1
SUCCESS = 0


class Node:
    """
    탐색트리에 사용되는 노드 클래스입니다.

    Attributes:
        key (int): 노드의 탐색값입니다.
        left (Node): 이진 트리로 연결되며 자신의 왼쪽 자식노드를 가리킵니다.
        right (Node): 이진 트리로 연결되며 자신의 오른쪽 자식노드를 가리킵니다.
        binkey (str): key값에 따른 이진수를 문자열입니다.
    """

    def __init__(self, key: int, left=None, right=None, compare: int = maxb):
        """
        노드를 초기화 해주는 함수입니다.


        Args:
            key (int): 노드의 데이터로 들어갈 값
            left (node): 자신의 자식노드 중 왼쪽 노드
            right (node): 자신의 자식노드 중 오른쪽 노드
            binkey (str): key값의 5자리 2진수 문자열
            compare (int): 패트리샤 트리에서 비교할 인덱스를 나타내는 정수


        Returns:
            None
        """

        self.__key = key
        self.__left = left
        self.__right = right
        self.__binkey = self.key_to_bin(key)[::-1]
        self.__compare = compare

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
    def binkey(self):
        return self.__binkey

    @binkey.setter
    def binkey(self, binkey):
        self.__binkey = binkey

    @property
    def compare(self):
        return self.__compare

    @compare.setter
    def compare(self, compare):
        self.__compare = compare

    def key_to_bin(self, key: int) -> str:
        """
        key값을 5자리의 2진수 형태로 나타내어 보여줍니다.    
        """
        temp_num = bin(key)[2:]
        return "0" * (maxb - len(temp_num)) + temp_num  # 5자리의 2진수로 수정


class Tree():
    """
    노드가 들어갈 트리 알고리즘의 뼈대입니다.

    Attributes:
        head (Node): 트리에서 루트가 되는 속성입니다.
    """

    def __init__(self) -> None:
        self.head: Node = Node(0)

    @abstractmethod
    def insert(self, key: int) -> int:
        """
        각 트리에 따른 노드를 넣는 함수입니다.

        Args:

            key (int): 노드의 key값을 넣기 위한 파라미터입니다.

        Returns:
            0: Success
            -2: Error
        """
        pass

    @abstractmethod
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

    @abstractmethod
    def check(self, key_list: list, time: float) -> None:
        """
        트리가 정확하게 구축되었는지 확인하여 출력해주는 메서드입니다.
        """
        pass
