"""Graph class with methods of various algorithms to solve it.
This operates as the model.

Desired algorithms:
Kruskal Algorithm
A*
"""
import collections
import random
from enum import Enum
import time

Coordinate = collections.namedtuple("coordinate", "x y")
Edge = collections.namedtuple("Edge", "neighbor distance")
#The maximum distance between two edges in the graph
MAX = 99999999999999999


class Graph:
    """A graph of verticies and edges."""

    def __init__(self, vertices=[], edges=[]):
        """
        :param vertices: (List)
        :param edges: (List of Tuple) pairs of verticies in an edge
        """
        self.vertices = vertices
        self.found = False
        for edge in edges:
            self.add_edge(edge[0], edge[1])
        self.start = self.vertices[0]

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, u, v):
        u.add_neighbor(v)
        v.add_neighbor(u)

    def get_target(self):
        target = self.vertices[len(self.vertices) - 1]
        for vertex in self.vertices:
            if vertex.get_status() is Status.TARGET:
                target = vertex
        return target

    #DOES NOT WORK
    #WRONG ALGORITHM TO CHOOSE. REVERSE THIS DECISION.
    def kruskal_algorithm(self):
        #TODo: Standarize naming conventions between algorithms.
        """
        Use Kruskal's algorithm to search through the entire graph.
        Note, this does not care about Vertex's that are starting, and does not terminate with target Vertex's.
        :return:
        """
        KruskalEdge = collections.namedtuple("KruskalEdge", "start end weight")
        obstacles = 0
        edges = []
        path = []
        for vertex in self.vertices:
            if vertex.status is not Status.OBSTACLE:
                for edge in vertex.edges:
                    if edge.neighbor.status is not Status.OBSTACLE:
                        edges.append(KruskalEdge(vertex, edge.neighbor, edge.distance))
            else:
                obstacles += 1
        while len(edges) > 0:
            #ToDO: Fix edges so that there aren't two edges of different weight between the same two verticies.
            current = self.min_edge(edges)
            edges.remove(current)
            path.append(current.start)
            path.append(current.end)
            if current.start.get_status() is Status.NORMAL:
                current.start.change_status(Status.NORMAL_VISITED, len(path))
            if current.end.get_status() is Status.NORMAL:
                current.end.change_status(Status.NORMAL_VISITED, len(path))
        return path

    def min_edge(self, edges):
        """
        Find the edge of least distance.
        :param edges: The edges generated.
        :return: (KruskalEdge) The one with the least distance.
        """
        min = MAX
        current = None
        for edge in edges:
            if edge.weight < min:
                min = edge.weight
                current = edge
        return current

    def a_star_algorithm(self):
        """Use the a* algorithm to find the target.
        Will stop if unfindable.
        """


    def dijkstra_algorithm(self):
        """Use Dijkstra's algorithm to search through the graph.
        Will only search through parts that are connected to self.get_start()
        Will not through the entirety of non-connected graph.
        """
        found = []
        missing = self.vertices.copy()
        distances = dict()
        start = self.get_start()
        distances.update({start : 0})
        while len(missing) > 0:
            current = self.get_min(distances, found)
            if current is None:
                return found
            found.append(current)
            missing.remove(current)
            if current.get_status() is Status.TARGET:
                return found
            if current.get_status() is Status.NORMAL:
               current.change_status(Status.NORMAL_VISITED, len(found))
            for edge in current.edges:
                distance = distances.get(current) + edge.distance
                if distance < distances.get(edge.neighbor, MAX):
                    distances.update({edge.neighbor : edge.distance})
        return found



    def prim_algorithm(self):
        """Use Prim's algorithm to search through the graph.
        Will only search through parts that are connected to self.get_start()
        Will not through the entirety of non-connected graph.
        """
        found = []
        distances = dict()
        for vertex in self.vertices:
            if vertex.status is not Status.OBSTACLE:
                distances.update({vertex : MAX})
        start = self.get_start()
        distances.update({start : 0})
        while len(distances) > 0:
            current = self.get_min(distances)
            #The path is unreachable.
            if current is None:
                return
            found.append(current)
            del distances[current]
            if current.get_status() is Status.TARGET:
                return found
            if current.get_status() is Status.NORMAL:
                current.change_status(Status.NORMAL_VISITED, len(found))
            for edge in current.edges:
                if edge.distance < distances.get(edge.neighbor, 0):
                    distances.update({edge.neighbor : edge.distance})

    def get_min(self, distances, found=[]):
        """
        Get the vertex that is the least distance.
        :param distances: Dict(Vertex, int) The vertex and its distance.
        :return: (Vertex) the vertex with the least distance.
        """
        closest = None
        min = MAX
        for vertex, distance in distances.items():
            if vertex in found:
                continue
            if distance < min:
                min = distance
                closest = vertex
        return closest

    def search(self, breadth):
        """
            Use breadth or depth first search on the Entire graph.
            :param breadth: (Boolean) If true, use bfs, if false use dfs
            :return: (List of Vertex) The verticies visited during the search
            """
        visited = []
        if breadth:
            self.little_bfs(self.get_start(), visited)
        else:
            self.little_dfs(self.get_start(), visited)
        for vertex in self.vertices:
            if vertex in visited or vertex.status is Status.OBSTACLE:
                continue
            if self.found:
                return visited
            if breadth:
                self.little_bfs(vertex, visited)
            else:
                self.little_dfs(vertex, visited)
        return visited

    def get_start(self):
        return self.start

    def little_search(self, vertex, visited, breadth, delay=False):
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
                self.found = True
                return visited
            if current not in visited and (current.status is Status.NORMAL or current.status is Status.START):
                visited.append(current)
                if current.status is Status.NORMAL:
                    current.change_status(Status.NORMAL_VISITED, len(visited))
                for neighbor in current.get_neighbors():
                    planned.append(neighbor)
        return visited

    def bfs(self):
        """
        Use breadth first search on the Entire graph.
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

    def reset(self, all=False):
        """
        Set this graph back to before it committed a search.
        :param: all (Boolean) Reset every vertex of every status to normal.
        :return: (Graph) self, indistinguishable from itself before mot recent search.
        """
        self.found = False
        for vertex in self.vertices:
            if all or vertex.new_status is Status.NORMAL_VISITED:
                vertex.change_status(Status.NORMAL)

    def immediate_update(self):
        """
        Immediately update every vertex to switch to its appropriate status.
        :return: None
        """
        for vertex in self.vertices:
            vertex.delay = 0


class MyGrid(Graph):
    """An extension of Graph using inheritance. Grid represents a 2 by 2 grid as a connected graph"""
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
        self.start = self.vertex_by_coordinate.get(Coordinate(0, 0))
        self.targets = []

    def mutate(self, coordinate, status):
        """
        Mutate the vertex of the given coordinates to have the given status.
        :param coordinate: (Coordinate) The x and y value of the vertex to be mutated.
        :param status: (Status) A vertex can be NORMAL, TARGET or OBSTACLE.
        :return: None
        """
        mutate = self.vertex_by_coordinate.get(coordinate)
        if status is Status.TARGET:
            self.targets.append(mutate)
        elif status is Status.START:
            self.start.change_status(Status.NORMAL)
            self.start = mutate
        mutate.change_status(status)


class Status(Enum):
    """The status of a vertex. The vertex has a different status for each color."""
    NORMAL = "white"
    NORMAL_VISITED = "blue"
    TARGET = "yellow"
    OBSTACLE = "black"
    START = "red"


class Vertex:
    """A vertex of the undirected graph."""

    def __init__(self, name, x=100, y=100):
        self.name = name
        self.edges = []
        self.x = x
        self.y = y
        self.delay = 0
        self.status = Status.NORMAL
        self.new_status = Status.NORMAL

    def add_neighbor(self, neighbor):
        distance = random.randrange(10)
        self.edges.append(Edge(neighbor, distance))

    def get_neighbors(self):
        """Get the verticies adjacent to this."""
        for edge in self.edges:
            yield edge.neighbor

    def get_color(self):
        """Get self's color based on self.status"""
        return self.get_status().value

    def get_status(self):
        """
        Get the current status. Then change self status if the delay is up.
        :return: The current status, which may be different from self.new_status
        """
        if self.delay <= 0:
            self.status = self.new_status
        else:
            self.delay -= 1
        return self.status

    #ToDo: Change to set_visited()
    def change_status(self, new_status, delay=0):
        """
        Change self's status to new_status after status has been asked for delay times.
        :param delay: The number of times status should be asked for before it is changed.
        :param new_status: What the status should be changed to.
        :return: The new status, even if it has not yet come into effect.
        """
        self.delay = delay
        self.new_status = new_status
        return new_status

if __name__ == "__main__":
    g = MyGrid()
    g.dijkstra_algorithm()