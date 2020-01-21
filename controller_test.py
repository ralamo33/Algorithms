import unittest
from controller import *
from algorithms import *
from gui import *


class MyTestCase(unittest.TestCase):
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
