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

def bfs(graph):
    """
    Use breadth first search to find the target Cell
    :param grid: (Graph) A two by two array.
    :return: (List of Vertex) The verticies visited during the search
    """
    visited = []
    planned = collections.deque()
    planned.append(graph.vertices[0])
    while len(planned) > 0:
        current = planned.popleft()
        if current not in visited:
            for neighbor in current.neighbors:
                    planned.append(neighbor)
            visited.append(current)
    return visited

def dfs(graph):
    """
    Use depth first search to find the target Cell
    :param grid: (Graph) A two by two array.
    :return: (List of Vertex) The verticies visited during the search
    """
    visited = []
    planned = collections.deque()
    planned.append(graph.vertices[0])
    while len(planned) > 0:
        current = planned.pop()
        if current not in visited:
            for neighbor in current.neighbors:
                    planned.append(neighbor)
            visited.append(current)
    return visited

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



    
