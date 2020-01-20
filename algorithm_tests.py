import unittest
from algorithms import *

class MyTestCase(unittest.TestCase):

    def test_bfs(self):
        v1 = Vertex("A")
        v2 = Vertex("B")
        v3 = Vertex("C")
        v4 = Vertex("D")
        v5 = Vertex("E")
        verticies = [v1, v2, v3, v4, v5]
        edges = [(v1, v2), (v2, v3), (v4, v5), (v1, v5)]
        graph = Graph(verticies, edges)
        self.assertEqual(bfs(graph), [v1, v2, v5, v3, v4])



if __name__ == '__main__':
    unittest.main()
