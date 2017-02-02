class Graph:
    def __init__(self):
        self.nodes = []
        self.arcs = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_arc(self, arc):
        self.arcs.append(arc)


class Node:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return '<Node instance: {}>'.format(self.key)


class Arc:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __repr__(self):
        return '<Arc instance: from {}, to {}, weight {}>'.format(self.from_node, self.to_node, self.weight)
