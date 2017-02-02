def minimum_spanning_tree(graph):
    tree = []
    visited = []

    start = graph.nodes[0]
    visited.append(start.key)

    while len(visited) < len(graph.nodes):
        next_arc = None

        for arc in graph.arcs:
            if (arc.from_node in visited and
                arc.to_node not in visited and
                (next_arc is None or arc.weight < next_arc.weight)):

                next_arc = arc

        visited.append(next_arc.to_node)
        tree.append(next_arc)

    return tree


if __name__ == '__main__':
  from graph import Graph, Node, Arc

  g = Graph()

  g.add_node(Node('A'))
  g.add_node(Node('B'))
  g.add_node(Node('C'))
  g.add_node(Node('D'))
  g.add_node(Node('E'))
  g.add_node(Node('F'))

  g.add_arc(Arc('A','B',1))
  g.add_arc(Arc('B','A',1))
  g.add_arc(Arc('A','E',3))
  g.add_arc(Arc('A','D',4))
  g.add_arc(Arc('B','D',4))
  g.add_arc(Arc('B','E',2))
  g.add_arc(Arc('C','E',4))
  g.add_arc(Arc('C','F',5))
  g.add_arc(Arc('D','A',4))
  g.add_arc(Arc('D','B',4))
  g.add_arc(Arc('D','E',4))
  g.add_arc(Arc('E','A',3))
  g.add_arc(Arc('E','B',2))
  g.add_arc(Arc('E','C',4))
  g.add_arc(Arc('E','D',4))
  g.add_arc(Arc('E','F',7))
  g.add_arc(Arc('F','C',5))
  g.add_arc(Arc('F','E',7))

  mst = minimum_spanning_tree(g)

  print(mst)
  print(sum(arc.weight for arc in mst))
