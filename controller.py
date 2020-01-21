"""The controller that communicates between algorithms and the view."""
from tkinter import Label

import algorithms as model
import gui as view
from enum import Enum
import PIL

class Algorithm(Enum):
    """Enums representing the algorithm selected."""
    BFS = "Breadth First Search"
    DFS = "Depth First Search"

class Controller:
    """Communicates between algorithms and gui."""

    def __init__(self, graph=model.MyGrid(), view=view.make_view()):
        self.model = graph
        self.view = view
        self.algorithm = Algorithm.BFS
        self.mutator = model.Status.NORMAL

    def mutate(self, x, y):
        """Mutate the tile of the given coordinates to the current mutator type."""
        self.model.mutate(model.Coordinate(x, y), self.mutator)


if __name__ == "__main__":
    c = Controller()

