"""Functions implementing several algorithms on a list.

Desired algorithms:
Dijstrka's Algorithm
Kruskal Algorithm
A*
"""
import collections


class Graph:
    """An unconnected graph of verticies and edges."""

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


class Vertex:
    """A vertex of the undirected graph."""

    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

def search(graph, breadth):
    """
        Use breadth or depth first search on the Entire graph.
        :param grid: (Graph) A two by two array.
        :param breadth: (Boolean) If true, use bfs, if false use dfs
        :return: (List of Vertex) The verticies visited during the search
        """
    visited = []
    for vertex in graph.vertices:
        if vertex in visited:
            continue
        if breadth:
            little_bfs(vertex, visited)
        else:
            little_dfs(vertex, visited)
    return visited

def little_search(vertex, visited, breadth):
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


def bfs(graph):
    """
    Use breadth first search on the Entire graph.
    :param grid: (Graph) A two by two array.
    :return: (List of Vertex) The verticies visited during the search
    """
    return search(graph, True)

def little_bfs(vertex, visited):
    """
    Use breadth first search on vertex and its neighbors.
    :param vertex: (Vertex) The start of the search.
    :param visited: (List of Vertex) Verticies that have alreaddy been visited.
    :return: The Verticies that were visited.
    """
    return little_search(vertex, visited, True)


def dfs(graph):
    """
    Use depth first search to find the target Cell
    :param grid: (Graph) A two by two array.
    :return: (List of Vertex) The verticies visited during the search
    """
    return search(graph, False)


def little_dfs(vertex, visited):
    """
        Use depth first search on vertex and its neighbors.
        :param vertex: (Vertex) The start of the search.
        :param visited: (List of Vertex) Verticies that have alreaddy been visited.
        :return: The Verticies that were visited.
        """
    return little_search(vertex, visited, False)


def display(verticies):
    """
    Display the given onto the console.
    :param verticies: (List of Vertex)
    :return:
    """
    for vertex in verticies:
        print(vertex.name)


if __name__ == "__main__":
    pass
