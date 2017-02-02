class Node():
    def __init__(self, key):
        self.key = key
        self.colour = RedBlackTree.RED
        self.parent = None
        self.left = None
        self.right = None


class RedBlackTree():
    BLACK, RED = 0, 1

    def __init__(self, root=None):
        self.root = root

    def left_rotate(self, node):
        y = node.right
        node.right = y.left

        if y.left is not None:
            y.left.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right

        if y.right is not None:
            y.right.parent = node

        y.parent = node.parent

        if node.parent is None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y

        y.right = node
        node.parent = y

    def insert(self, node):
        y = None
        x = self.root

        while x is not None:
            y = x
            x = x.left if node.key < x.key else x.right

        node.parent = y
        
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
