
from typing import Tuple


TEXT_LENGTH = 27


class Node:
    """
    탐색트리에 사용되는 노드 클래스입니다.

    Attributes:
        key (int): 노드의 탐색값입니다.
        left (Node): 이진 트리로 연결되며 자신의 왼쪽 자식노드를 가리킵니다.
        right (Node): 이진 트리로 연결되며 자신의 오른쪽 자식노드를 가리킵니다.
    """

    def __init__(self, key: int, left=None, right=None) -> None:
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


class Huffman():
    """
    허프만 트리 알고리즘에 해당하는 클래스입니다.

    Attributes:
        text (str): 문자열 값입니다. 이 값을 가지고 허프만 트리 알고리즘이 만들어집니다.
    """

    def __init__(self, text: str) -> None:
        self.__text: str = text
        self.__k, self.__count = self.__calc_count(text)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def count(self):
        return self.__count

    @property
    def k(self):
        return self.__k

    def __index_to_string(self, index: int) -> str:
        """
        인덱스 값에 따라 spacing 또는 알파벳을 리턴합니다.
        그렇기에 index의 값이 27 이상이 되어서는 안되며 0과 26 사이어야 합니다
        """
        if index == 0:
            return " "
        elif index > 26:
            return -1  # out of index
        else:
            return chr(index+64)

    def __calc_count(self, text: str) -> Tuple[list, list]:
        """
        count 리스트를 구하여 리턴합니다.
        """
        k = []
        count = []
        for i in range(TEXT_LENGTH):
            frequency = text.count(self.__index_to_string(i))  # 빈도수 구함
            if frequency == 0:
                continue
            k.append(i)
            count.append(frequency)
        return k, count


if __name__ == "__main__":
    text = "A SIMPLE STRING TO BE ENCODED USING A MINIMAL NUMBER OF BITS"
    d = Huffman(text)
    print(len(d.count))
    print(len(d.k))
