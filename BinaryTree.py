class Node():
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data

    def __str__(self):
        return '{} {}'.format(self.key, self.data)


class Tree():
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, data=None):
        child = Node(key, data)

        if self.root is None:
            self.root = child
        else:
            self._insert(child, self.root)

    def _insert(self, child, node):
        if child.key < node.key:
            if node.left is None:
                node.left = child
            else:
                self._insert(child, node.left)
        else:
            if node.right is None:
                node.right = child
            else:
                self._insert(child, node.right)

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if key == node.key:
            return node
        if key < node.key and node.left is not None:
            return self._find(key, node.left)
        if key > node.key and node.right is not None:
            return self._find(key, node.right)

    def __str__(self):
        if self.root is not None:
            return self._print(self.root)

    def _print(self, node):
        out = ''
        if node is not None:
            out += self._print(node.left)
            out += str(node) + ' '
            out += self._print(node.right) + '\n'
        return out


if __name__ == '__main__':
    tree = Tree()

    tree.insert(3, 'hello')
    tree.insert(7, 'world')
    tree.insert(1, 'asdf')
    tree.insert(5, 'qwerty')

    print(tree, end='')
    print(tree.find(3))
    print(tree.find(2))
