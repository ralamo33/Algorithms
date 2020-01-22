import unittest
from controller import *
from graph import *
from gui import *


class MyTestCase(unittest.TestCase):
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")
    v5 = Vertex("E")
    verticies = [v1, v2, v3, v4, v5]
    edges = [(v1, v2), (v2, v3), (v4, v5), (v1, v5)]
    graph = Graph(verticies, edges)
    controller = Controller(graph)

    def test_run(self):
        self.controller.algorithm = Graph.bfs
        self.assertEqual(self.controller.run(), [self.v1, self.v2, self.v5, self.v3, self.v4])
        self.controller.algorithm = Graph.dfs
        self.assertEqual(self.controller.run(), [self.v1, self.v5, self.v4, self.v2, self.v3])
        self.controller = Controller(self.graph)



    def test_mutate(self):
        c = Controller()
        c.mutator = Status.OBSTACLE
        c.mutate(3, 3)
        vertex = c.model.vertex_by_coordinate.get(Coordinate(3,3))
        self.assertEqual(Status.OBSTACLE, vertex.status)
        c.mutator = Status.TARGET
        c.mutate(0, 0)
        vertex = c.model.vertex_by_coordinate.get(Coordinate(0, 0))
        self.assertEqual(Status.TARGET, vertex.status)
        c.mutator = Status.NORMAL
        c.mutate(0, 0)
        self.assertEqual(Status.NORMAL, vertex.status)






if __name__ == '__main__':
    unittest.main()
