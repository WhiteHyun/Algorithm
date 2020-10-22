from homework7.node import Node


class Tree():
    """
    노드가 들어갈 트리 알고리즘의 뼈대입니다.
    """

    def __init__(self) -> None:
        self.head = Node(1)


if __name__ == "__main__":
    d = Tree()
    print(d.head)
