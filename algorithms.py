"""Graph class with methods of various algorithms to solve it.
This operates as the model.

Desired algorithms:
Dijstrka's Algorithm
Kruskal Algorithm
A*
"""
import collections
import random
from enum import Enum

Coordinate = collections.namedtuple("coordinate", "x y")

class Graph:
    """A graph of verticies and edges."""

    def __init__(self, vertices=[], edges=[]):
        """
        :param vertices: (List)
        :param edges: (List of Tuple) pairs of verticies in an edge
        """
        self.vertices = vertices
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, u, v):
        u.add_neighbor(v)
        v.add_neighbor(u)

    def search(self, breadth):
        """
            Use breadth or depth first search on the Entire graph.
            :param grid: (Graph) A two by two array.
            :param breadth: (Boolean) If true, use bfs, if false use dfs
            :return: (List of Vertex) The verticies visited during the search
            """
        visited = []
        for vertex in self.vertices:
            if vertex in visited or vertex.status is Status.OBSTACLE:
                continue
            if breadth:
                self.little_bfs(vertex, visited)
            else:
                self.little_dfs(vertex, visited)
        return visited

    def little_search(self, vertex, visited, breadth):
        """
        Use breadth first search on vertex and its neighbors.
        :param vertex: (Vertex) The start of the search.
        :param visited: (List of Vertex) Verticies that have alreaddy been visited.
        :param breadth: (Boolean) Use bfs if trues, use dfs otherwise
        :return: The Verticies that were visited.
        """
        planned = collections.deque()
        planned.append(vertex)
        while len(planned) > 0:
            if breadth:
                current = planned.popleft()
            else:
                current = planned.pop()
            if current.status is Status.TARGET:
                visited.append(current)
                return visited
            if current not in visited and current.status is Status.NORMAL:
                visited.append(current)
                current.status = Status.NORMAL_VISITED
                for neighbor in current.neighbors:
                    planned.append(neighbor)
        return visited

    def bfs(self):
        """
        Use breadth first search on the Entire graph.
        :param grid: (Graph) A two by two array.
        :return: (List of Vertex) The verticies visited during the search
        """
        return self.search(True)

    def little_bfs(self, vertex, visited):
        """
        Use breadth first search on vertex and its neighbors.
        :param vertex: (Vertex) The start of the search.
        :param visited: (List of Vertex) Verticies that have alreaddy been visited.
        :return: The Verticies that were visited.
        """
        return self.little_search(vertex, visited, True)

    def dfs(self):
        """
        Use depth first search to find the target Cell
        :param grid: (Graph) A two by two array.
        :return: (List of Vertex) The verticies visited during the search
        """
        return self.search(False)

    def little_dfs(self, vertex, visited):
        """
            Use depth first search on vertex and its neighbors.
            :param vertex: (Vertex) The start of the search.
            :param visited: (List of Vertex) Verticies that have alreaddy been visited.
            :return: The Verticies that were visited.
            """
        return self.little_search(vertex, visited, False)

    def reset(self):
        """
        Set this graph back to before it committed a search.
        :return: (Graph) self, indistinguishable from itself before mot recent search.
        """
        for vertex in self.vertices:
            if vertex.status is Status.NORMAL_VISITED:
                vertex.status = Status.NORMAL

class MyGrid:
    """An extension of Graph using compisition. Grid represents a 2 by 2 grid as a connected graph"""
    def __init__(self, rows=10, cols=10):
        """
        Create a two by two grid.
        :param rows: (int) THe number of rows on the grid.
        :param cols: (int) THe number of columns
        :param window_width: (int) The width of the grid.
        :param window_height: (int) The height of the grid.
        :return: (Graph) A two by two grid of size rows * cols, where its image is window_width by window_height.
        """
        self.rows = rows
        self.cols = cols
        """self.vertex_width = window_width / cols
        self.vertex_height = window_height / rows"""
        self.vertex_by_coordinate = dict()
        self.vertices = []
        edges = []
        for y in range(rows):
            for x in range(cols):
                self.vertex_by_coordinate.update({Coordinate(x, y): Vertex("grid", x, y)})
        for cord, vertex in self.vertex_by_coordinate.items():
            self.vertices.append(vertex)
            if cord.x > 0:
                other = self.vertex_by_coordinate.get(Coordinate(cord.x - 1, cord.y))
                edges.append((vertex, other))
            if cord.y > 0:
                other = self.vertex_by_coordinate.get(Coordinate(cord.x, cord.y - 1))
                edges.append((vertex, other))
            if cord.x < cols - 1:
                other = self.vertex_by_coordinate.get(Coordinate(cord.x + 1, cord.y))
                edges.append((vertex, other))
            if cord.y < cols - 1:
                other = self.vertex_by_coordinate.get(Coordinate(cord.x, cord.y + 1))
                edges.append((vertex, other))
        self.edges = edges
        self.graph = Graph(self.vertices, self.edges)

    def search(self, breadth):
        return self.graph.search(breadth)

    def bfs(self):
        """Breadth first search"""
        return self.graph.bfs()

    def dfs(self):
        """Depth first search"""
        return self.graph.dfs()

    def mutate(self, coordinate, status):
        """
        Mutate the vertex of the given coordinates to have the given status.
        :param coordinate: (Coordinate) The x and y value of the vertex to be mutated.
        :param status: (Status) A vertex can be NORMAL, TARGET or OBSTACLE.
        :return: None
        """
        self.vertex_by_coordinate.get(coordinate).status = status

class Status(Enum):
    """The status of a vertex. The vertex has a different status for each color."""
    NORMAL = "white"
    NORMAL_VISITED = "red"
    TARGET = "yellow"
    OBSTACLE = "black"


class Vertex:
    """A vertex of the undirected graph."""

    def __init__(self, name, x=100, y=100, distance=random.randrange(10)):
        self.name = name
        self.distance = distance
        self.neighbors = []
        self.x = x
        self.y = y
        self.status = Status.NORMAL

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_color(self):
        """Get self's color based on self.status"""
        return self.status.value

    """def draw(self, width, height):
        display = Image.new("RGB", (width, height), self.color)
        return ImageOps.expand(display, 1)"""

def display(verticies):
    """
    Display the given onto the console.
    :param verticies: (List of Vertex)
    :return:
    """
    for vertex in verticies:
        print(vertex.x, vertex.y)


if __name__ == "__main__":
    grid = MyGrid()
    pass

