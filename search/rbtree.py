if __name__ == "__main__" or __name__ == "rbtree":
    from common.tree import *
else:
    from .common.tree import *


class RBTree:
    """
    레드블랙트리 알고리즘

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

    def insert_case_1(self, node: RBNode):
        """
        Default case.
        Given node is root.
        """
        if node.parent is None:
            node.color = RBNode.BLACK
        else:
            self.insert_case_2(node)

    def insert_case_2(self, node: RBNode):
        """
        Second case.
        Given node is not root.
        Parent node is black.
        """
        if node.parent.color == RBNode.BLACK:
            return
        else:
            self.insert_case_3(node)

    def insert_case_3(self, node: RBNode):
        """
        Third case.
        Given node is not root.
        Parent node is not black
        Uncle is red.
        """
        uncle: Node = node.uncle()
        if uncle is not None and uncle.color == RBNode.RED:
            node.parent.color = RBNode.BLACK
            uncle.color = RBNode.BLACK
            # uncle노드가 있다는 것은 Grandparent 노드도 존재
            grandparent: Node = node.grandparent()
            grandparent.color = RBNode.RED

            self.insert_case_1(grandparent)
        else:
            self.insert_case_4(node)

    def insert_case_4(self, node: RBNode):
        """
        Fourth case.
        Given node is not root.
        Parent node is not black.
        Uncle is not red.
        Ready or not ready for rotation
        """

        grandparent: Node = node.grandparent()
        parent: Node = node.parent

        if parent.right == node and grandparent.left == parent:
            self.rotate_left(parent)
            node = node.left
        elif parent.left == node and grandparent.right == parent:
            self.rotate_right(parent)
            node = node.right

        self.insert_case_5(node)

    def insert_case_5(self, node: RBNode):
        """
        Fifth case.
        Given node is not root.
        Parent node is not Black.
        Uncle node is not Red.
        Ready for rotation.
        """

        grandparent: Node = node.grandparent()
        parent: Node = node.parent

        grandparent.color = RBNode.RED
        parent.color = RBNode.BLACK

        if parent.left == node:
            self.rotate_right(grandparent)

        if parent.parent is None:
            self.root = parent

    def insert(self, key_to_insert, verbose=False):
        if self.is_empty():
            # Empty?
            self.root = RBNode(key=key_to_insert, color=RBNode.BLACK)
            return

        closest: Node = binary_search(
            root=self.root, key_to_find=key_to_insert, find_closest=True, verbose=verbose)
        if closest is None:
            # Already exists?
            return

        # Just insert first.
        new_node = RBNode(key=key_to_insert, color=RBNode.RED, parent=closest)
        go_left = (key_to_insert < closest.key)

        if go_left:
            closest.left = new_node
        else:
            closest.right = new_node

        # Do extra things.
        self.insert_case_1(new_node)

    def dump(self, visited=None, verbose=True):
        dump(self.root, visited=visited, verbose=verbose)


@staticmethod
def insert_test():
    tree = RBTree()
    [tree.insert(x) for x in [27, 13, 8, 17, 1, 11, 15, 25, 6, 22]]

    tree_by_hand = RBTree()
    node27r = RBNode(key=27, color=RBNode.RED)
    node22r = RBNode(key=22, color=RBNode.RED)
    node6r = RBNode(key=6, color=RBNode.RED)
    node25b = RBNode(key=25, color=RBNode.BLACK, left=node22r, right=node27r)
    node15b = RBNode(key=15, color=RBNode.BLACK)
    node11b = RBNode(key=11, color=RBNode.BLACK)
    node1b = RBNode(key=1, color=RBNode.BLACK, right=node6r)
    node17r = RBNode(key=17, color=RBNode.RED, left=node15b, right=node25b)
    node8r = RBNode(key=8, color=RBNode.RED, left=node1b, right=node11b)
    node13b = RBNode(key=13, color=RBNode.BLACK, left=node8r, right=node17r)
    node27r.parent = node25b
    node22r.parent = node25b
    node6r.parent = node1b
    node1b.parent = node8r
    node11b.parent = node8r
    node15b.parent = node17r
    node25b.parent = node17r
    node8r.parent = node13b
    node17r.parent = node13b
    tree_by_hand.root = node13b

    return "Success" if tree.equals(tree_by_hand) else "Fail"


if __name__ == "__main__":
    from common.invoker import from_input

    tree = RBTree()
    def insert(key, verbose): return tree.insert(int(key), verbose)

    def search(key, verbose): return True if tree.search(
        int(key), verbose) is not None else False
    from_input(insert, search)
