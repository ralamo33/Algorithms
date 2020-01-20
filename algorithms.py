"""Functions implementing several algorithms on a list.

Desired algorithms:
Breadth First Search (BFS)
Dijstrka's Algorithm
Kruskal Algorithm
A*
"""

import collections

class Grid:
    """A two by two grid that can be traversed by an algorithm."""
    class Cell:
        """A single Cell of the grid."""        
        def __init__(self, row, col):
            self.row = row
            self.col = col
            self.target = False

        def display(self):
            """
            Turn this into a string for viewing.
            :return: (String) representing self.
            """
            image = [str(self.row), str(self.col)]
            if self.target:
                image.append("*")
            return " ".join(image)

    def __init__(self, width, height):
        """
        Create a Grid.
        :param width: (int) The width of the grid.
        :param height: (int) The height of the grid.
        """
        self.width = width
        self.height = height
        self.board = [[self.Cell(i, j) for i in range(width)] for j in range(height)]

    def get_origin(self):
        """
        Get the tile where self begins.
        :return: (Tile) The starting point of self.
        """
        return self.board[0][0]
    
    def get_neighbors(self, tile):
        """
        Get the neighbors of the given 
        :param tile: (Tile) Find the neighbors of this.
        :return: (List) The neighbors of tile.
        """
        neighbors = []
        row = tile.row
        col = tile.col
        if row > 0:
            neighbors.append(self.board[row - 1][col])
        if col > 0:
            neighbors.append(self.board[row][col - 1])
        if row < self.height - 1:
            neighbors.append(self.board[row + 1][col])
        if col < self.width - 1:
            neighbors.append(self.board[row][col + 1])
        return neighbors
        
        

    def set_target(self, row, col):
        """
        Make a Cell the target.
        :param row: The row of the new target.
        :param col: The column of the new target.
        :return: self
        """
        self.board[row][col].target = True
        return self

def bfs(grid=Grid(5, 5).set_target(2, 2)):
    """
    Use breadth first search to find the target Cell
    :param grid: (Grid) A two by two array.
    :return: (List) The path the function took.
    """
    current = grid.get_origin()
    path = []
    future = collections.deque()
    while not current.target:
        for neighbor in grid.get_neighbors(current):
            if neighbor not in path and neighbor not in future:
                future.append(neighbor)
        current = future.popleft()
        path.append(current)
    return path

if __name__ == "__main__":
    path = bfs()
    image = []
    for step in path:
        image.append(step.display())
    print("   ".join(image))



    
