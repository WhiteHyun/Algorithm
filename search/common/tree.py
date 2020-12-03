"""
Some helpful things for tree implementation.
"""


class Node:
    """
    >>> Node(3) == Node(3)
    True

    >>> str(Node(4))
    "Key: 4, Left: -, Right: -."
    """

    def __init__(self, key, left=None, right=None) -> None:
        self.key = key
        self.left = left
        self.right = right

    def __str__(self) -> str:
        left = str(self.left.key) if self.left is not None else "-"
        right = str(self.right.key) if self.right is not None else "-"

        return f"Key: {self.key}, Left: {left}, Right: {right}."

    def __eq__(self, o: object) -> bool:
        if type(self) != type(o):
            return False

        return ((self.key == o.key)
                and ((self.left.key if self.left is not None else None) == (o.left.key if o.left is not None else None))
                and ((self.right.key if self.right is not None else None) == (o.right.key if o.right is not None else None)))

    def __hash__(self) -> int:
        return hash(("key", self.key, "left", self.left.key if self.left is not None else None, "right", self.right.key if self.right is not None else None))


class RBNode(Node):
    """
    >>> RBNode(3, color=RBNode.BLACK) == RBNode(3, color=RBNode.BLACK)
    True

    >>> str(RBNode(3, color=RBNode.BLACK))
    'Key: 3, Color: BLACK, Left: -, Right: -.'

    >>> RBNode.family_test()
    'Success'
    """
    BLACK = 0
    RED = 1

    def __init__(self, key, color=BLACK, left=None, right=None, parent=None) -> None:
        Node.__init__(self, key=key, left=left, right=right)
        self.color = color
        self.parent = parent

    def __str__(self) -> str:
        color = "BLACK" if self.color == self.BLACK else "RED"
        left = self.left.key if self.left is not None else "-"
        right = self.right.key if self.right is not None else "-"
        return f"Key: {self.key}, Color: {color}, Left: {left}, Right: {right}."

    def __eq__(self, o: object) -> bool:
        if type(self) != type(o):
            # Only accepts same type.
            return False

        return Node.__eq__(self, o) and self.color == o.color and self.parent == o.parent

    def __hash__(self) -> int:
        return hash(("key", self.key, "color", self.color, "left", self.left.key if self.left is not None else None, "right", self.right.key if self.right is not None else None, "parent", self.parent))

    def grandparent(self):
        if self.parent is None:
            return None

        return self.parent.parent

    def uncle(self):
        gp = self.grandparent()
        if gp is None:
            return None

        return gp.right if self.parent == gp.left else gp.left

    def sibling(self):
        if self.parent.left == self:
            return self.parent.right
        else:
            return self.parent.left

    @staticmethod
    def family_test():
        node17 = RBNode(key=17, color=RBNode.RED)
        node13 = RBNode(key=12, color=RBNode.BLACK, right=node17)
        node1 = RBNode(key=1, color=RBNode.BLACK)
        node8 = RBNode(key=8, color=RBNode.BLACK, left=node1, right=node13)

        node17.parent = node13
        node13.parent = node8
        node1.parent = node8

        root: Node = node8

        parent_test = (node1.parent == node8) and (node17.parent == node13)
        grandparent_test = (node17.grandparent() == node8)
        uncle_test = (node17.uncle() == node1)
        sibling_test = (node13.sibling() == node1)

        return "Success" if parent_test and grandparent_test and uncle_test and sibling_test else "Fail"


def left(root: int):
    """
    >>> left(0)
    1

    >>> left(1)
    3

    >>> left(3)
    7
    """
    return (root << 1) + 1


def right(root: int):
    """
    >>> right(0)
    2

    >>> right(1)
    4

    >>> right(3)
    8
    """
    return (root << 1) + 2


def parent(child: int):
    """
    >>> parent(3)
    1
    >>> parent(4)
    1
    >>> parent(2)
    0
    """
    return (child - 1) >> 1


def binary_search(root: Node, key_to_find, find_closest=True, verbose=False):
    """
    Perform a binary search from root node.

    Params:
        key_to_find (comparable): A key to find in the tree.
        find_closest (bool): Return the closest node if search failed.

    Returns:
        if key found and find_closest: the node.
        if key found and not find_closest: None.
        if key not found and find_closest: the closest node.
        if key not found and not find_closest: None.
    """
    current_node: Node = root
    last_node: Node = None

    while current_node is not None:
        if current_node.key == key_to_find:
            # Found in the middle
            break

        # In this BST implementation, nodes who are smaller than the key
        # goes left, and those equal to or bigger than the key goes right.
        go_left = (key_to_find < current_node.key)

        last_node = current_node
        current_node = current_node.left if go_left else current_node.right

    if current_node is None:
        # Not found
        return last_node if find_closest else None
    else:
        # Found
        return None if find_closest else current_node


def dump(root, visited=[], verbose=True):
    if root is None:
        return

    if visited is not None:
        if root in visited:
            return
        else:
            visited.append(root)

    if verbose:
        print(root)

    dump(root=root.left, visited=visited, verbose=verbose)
    dump(root=root.right, visited=visited, verbose=verbose)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
