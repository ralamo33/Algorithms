"""Functions implementing several algorithms on a list.

Desired algorithms:
Dijstrka's Algorithm
Kruskal Algorithm
A*
"""
import collections
import random

class Graph:
    """A graph of verticies and edges."""

    def __init__(self, vertices=[], edges=[], width=500, height=500):
        """
        :param vertices: (List)
        :param edges: (List of Tuple) pairs of verticies in an edge
        """
        self.width = width
        self.height = height
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
            if vertex in visited:
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
            if current not in visited:
                for neighbor in current.neighbors:
                    planned.append(neighbor)
                visited.append(current)
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

class Grid:
    """An extension of Graph using compisition. Grid represents a 2 by 2 grid as a connected graph"""
    def __init__(self, rows, cols, window_width=500, window_height=500):
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
        verticies = dict()
        Coordinate = collections.namedtuple("coordinate", "x y")
        edges = []
        for y in range(rows):
            for x in range(cols):
                verticies.update({Coordinate(x, y): Vertex("grid", x, y)})
        for cord, vertex in verticies.items():
            if cord.x > 0:
                other = verticies.get(Coordinate(cord.x - 1, cord.y))
                edges.append((vertex, other))
            if cord.y > 0:
                other = verticies.get(Coordinate(cord.x, cord.y - 1))
                edges.append((vertex, other))
            if cord.x < cols - 1:
                other = verticies.get(Coordinate(cord.x + 1, cord.y))
                edges.append((vertex, other))
            if cord.y < cols - 1:
                other = verticies.get(Coordinate(cord.x, cord.y + 1))
                edges.append((vertex, other))
        self.graph = Graph(verticies, edges, window_width, window_height)

    def bfs(self):
        """Breadth first search"""
        return self.graph.bfs()

    def dfs(self):
        """Depth first search"""
        return self.graph.dfs()



class Vertex:
    """A vertex of the undirected graph."""

    def __init__(self, name, x=100, y=100, distance=random.randrange(10)):
        self.name = name
        self.distance = distance
        self.neighbors = []
        self.x = x
        self.y = y
        self.color = "white"

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

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
    Graph = create_grid(3, 3)
    display(Graph.vertices)

