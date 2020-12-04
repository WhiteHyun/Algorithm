if __name__ == "__main__" or __name__ == "rbtree":
    from common.tree import *
else:
    from .common.tree import *


class RBTree:
    """
    >>> RBTree.insert_test()
    "Success"
    """

    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return (self.root is None)

    def equals(self, other):
        this_nodes = list()
        self.dump(visited=this_nodes, verbose=False)

        other_nodes = list()
        other.dump(visited=other_nodes, verbose=False)

        return this_nodes == other_nodes

    def search(self, key_to_find, verbose=False):
        """
        Perform a binary search on this RB tree.
        Return None if not found.
        """
        if self.is_empty():
            return None

        return binary_search(root=self.root, key_to_find=key_to_find, find_closest=False, verbose=verbose)

    def rotate_left(self, node: RBNode):
        child: Node = node.right
        parent: Node = node.parent

        node.right = child.left
        if child.left is not None:
            child.left.parent = node
        node.parent = child
        child.left = node
        child.parent = parent

        if parent is not None:
            if parent.left == node:
                parent.left = child
            else:
                parent.right = child

    def rotate_right(self, node: RBNode):
        child: Node = node.left
        parent: Node = node.parent

        node.left = child.right
        if child.right is not None:
            child.right.parent = node
        node.parent = child
        child.right = node
        child.parent = parent

        if parent is not None:
            if parent.right == node:
                parent.right = child
            else:
                parent.left = child

    def dump(self, visited=None, verbose=True):
        dump(self.root, visited=visited, verbose=verbose)


if __name__ == "__main__":
    from common.invoker import from_input

    tree = RBTree()
    def insert(key, verbose): return tree.insert(int(key), verbose)

    def search(key, verbose): return True if tree.search(
        int(key), verbose) is not None else False
    from_input(insert, search)
