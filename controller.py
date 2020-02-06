"""The controller that communicates between algorithms and the view."""
from tkinter import Label

import graph as model
from enum import Enum
import PIL

class Controller:
    """Communicates between algorithms and gui."""

    def __init__(self, graph=model.MyGrid()):
        self.model = graph
        self.algorithm = model.Graph.bfs
        self.mutator = model.Status.NORMAL

    def set_obstacle(self):
        """Set the mutator as an obstacle."""
        self.mutator = model.Status.OBSTACLE

    def set_target(self):
        self.mutator = model.Status.TARGET

    def set_normal(self):
        self.mutator = model.Status.NORMAL

    def set_start(self):
        self.mutator = model.Status.START
        
    def set_dfs(self):
        self.algorithm = model.Graph.dfs
        
    def set_bfs(self):
        self.algorithm = model.Graph.bfs

    def set_prim(self):
        self.algorithm = model.Graph.prim_algorithm

    def set_dijkstra(self):
        self.algorithm = model.MyGrid.dijkstra_algorithm

    def set_a_star(self):
        self.algorithm = model.MyGrid.a_star_algorithm

    def mutate(self, x, y):
        """Mutate the tile of the given coordinates to the current mutator type."""
        self.model.mutate(model.Coordinate(x, y), self.mutator)

    def immediate_update(self):
        """Immediately complete an algorithm run."""
        self.model.immediate_update()

    def reset_all(self):
        """Reset all Vertex in the graph to normal."""
        self.model.reset(True)

    def reset(self):
        """Reset all Vertex that were found to not found"""
        self.model.reset(False)

    def run(self):
        """Run an algorithm on the model."""
        return self.model.run()

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



