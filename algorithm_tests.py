import unittest
from algorithms import *

class MyTestCase(unittest.TestCase):
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")
    v5 = Vertex("E")
    verticies = [v1, v2, v3, v4, v5]
    edges = [(v1, v2), (v2, v3), (v4, v5), (v1, v5)]
    graph = Graph(verticies, edges)

    u1 = Vertex("A")
    u2 = Vertex("B")
    u3 = Vertex("C")
    u4 = Vertex("D")
    u5 = Vertex("E")
    u6 = Vertex("F")
    u7 = Vertex("G")
    u8 = Vertex("H")
    verticies2 = [u1, u2, u3, u4, u5, u6, u7, u8]
    edges2 = [(u1, u8), (u1, u7), (u1, u6), (u1, u2), (u2, u3), (u4, u5)]
    graph2 = Graph(verticies2, edges2)

    def test_bfs(self):
        self.graph.reset()
        self.graph2.reset()
        self.assertEqual(self.graph.bfs(), [self.v1, self.v2, self.v5, self.v3, self.v4])
        self.graph.reset()
        self.assertEqual(self.graph2.little_bfs(self.u1, []), [self.u1, self.u8, self.u7, self.u6, self.u2, self.u3])
        self.graph2.reset()
        self.assertEqual(self.graph2.bfs(), [self.u1, self.u8, self.u7, self.u6, self.u2, self.u3, self.u4, self.u5])
        self.graph2.reset()


    def test_dfs(self):
        self.graph.reset()
        self.assertEqual(self.graph.dfs(), [self.v1, self.v5, self.v4, self.v2, self.v3])
        self.graph.reset()
        self.graph2.reset()
        self.assertEqual(self.graph2.little_dfs(self.u1, []), [self.u1, self.u2, self.u3, self.u6, self.u7, self.u8])
        self.graph2.reset()
        self.assertEqual(self.graph2.dfs(), [self.u1, self.u2, self.u3, self.u6, self.u7, self.u8, self.u4, self.u5])
        self.graph2.reset()


if __name__ == '__main__':
    unittest.main()
