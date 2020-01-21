"""The controller that communicates between algorithms and the view."""
from tkinter import Label

import algorithms as model
import gui as view
from enum import Enum
import PIL

class Controller:
    """Communicates between algorithms and gui."""

    def __init__(self, graph=model.MyGrid(), view=view.make_view()):
        self.model = graph
        self.view = view
        self.algorithm = model.Graph.bfs
        self.mutator = model.Status.NORMAL

    def mutate(self, x, y):
        """Mutate the tile of the given coordinates to the current mutator type."""
        self.model.mutate(model.Coordinate(x, y), self.mutator)

    def run(self):
        """Run an algorithm on the model."""
        return self.algorithm(self.model)


if __name__ == "__main__":
    c = Controller()
    mine = model.MyGrid.bfs
    grid = model.MyGrid()
    answers = mine(grid)


