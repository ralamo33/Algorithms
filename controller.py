"""The controller that communicates between algorithms and the view."""
from tkinter import Label

import algorithms as model
from enum import Enum
import PIL

class Controller:
    """Communicates between algorithms and gui."""

    def __init__(self, graph=model.MyGrid()):
        self.model = graph
        self.algorithm = model.Graph.bfs
        self.mutator = model.Status.NORMAL

    def mutate(self, x, y):
        """Mutate the tile of the given coordinates to the current mutator type."""
        self.model.mutate(model.Coordinate(x, y), self.mutator)

    def run(self):
        """Run an algorithm on the model."""
        return self.algorithm(self.model)

    def get_rows(self):
        """Get the number of rows of the model."""
        return self.model.rows

    def get_cols(self):
        """Get the number of columns of the model."""
        return self.model.cols

    def get_verticies(self):
        """
        Get the verticies of the model.
        :return: (List of Vertex)
        """
        return self.model.vertices




if __name__ == "__main__":
    c = Controller()
    mine = model.MyGrid.bfs
    grid = model.MyGrid()
    answers = mine(grid)


