"""Graph class with methods of various algorithms to solve it.
This operates as the model.

Desired algorithms:
Kruskal Algorithm
A*
"""
import collections
import random
from enum import Enum
import math
import time

Coordinate = collections.namedtuple("coordinate", "x y")
Edge = collections.namedtuple("Edge", "neighbor distance")
#The maximum distance between two edges in the graph
MAX = 999999
MaxWeight = 10

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
        self.targets = set()
        self.searching = False

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, u, v):
        u.add_neighbor(v)
        v.add_neighbor(u)

    def get_targets(self):
        """
        Get the number of targets in this graph. Or if there are none return 1, ensuring the search does not end early.
        :return: (int) The number of targets in the graph.
        """
        if len(self.targets) == 0:
            return 1
        return len(self.targets)

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


    def dijkstra_algorithm(self):
        """Use Dijkstra's algorithm to search through the graph.
        Will only search through parts that are connected to self.get_start()
        Will not through the entirety of non-connected graph.
        """
        self.searching = True
        visited = []
        find = self.get_targets()
        missing = self.vertices.copy()
        distances = dict()
        start = self.get_start()
        distances.update({start : 0})
        while len(missing) > 0 and find > 0:
            current = self.get_min(distances, visited)
            if current is None:
                return visited
            visited.append(current)
            missing.remove(current)
            if current.get_status() is Status.TARGET:
                find -= 1
            if current.get_status() is Status.NORMAL:
               current.change_status(Status.NORMAL_VISITED, len(visited))
            for edge in current.edges:
                distance = distances.get(current) + edge.distance
                if distance < distances.get(edge.neighbor, MAX):
                    distances.update({edge.neighbor : edge.distance})
        return visited



    def prim_algorithm(self):
        """Use Prim's algorithm to search through the graph.
        Will only search through parts that are connected to self.get_start()
        Will not through the entirety of non-connected graph.
        """
        self.searching = True
        visited = []
        find = self.get_targets()
        distances = dict()
        for vertex in self.vertices:
            if vertex.status is not Status.OBSTACLE:
                distances.update({vertex : MAX})
        start = self.get_start()
        distances.update({start : 0})
        while len(distances) > 0 and find > 0:
            current = self.get_min(distances)
            #The path is unreachable.
            if current is None:
                return
            visited.append(current)
            del distances[current]
            if current.get_status() is Status.TARGET:
                find -= 1
            if current.get_status() is Status.NORMAL:
                current.change_status(Status.NORMAL_VISITED, len(visited))
            for edge in current.edges:
                if edge.distance < distances.get(edge.neighbor, 0):
                    distances.update({edge.neighbor : edge.distance})

    def get_min(self, distances, visited=[]):
        """
        Get the vertex that is the least distance.
        :param distances: Dict(Vertex, int) The vertex and its distance.
        :return: (Vertex) the vertex with the least distance.
        """
        closest = None
        min = MAX
        for vertex, distance in distances.items():
            if vertex in visited:
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
        self.searching = True
        visited = []
        self.find = self.get_targets()
        print(self.find)
        if breadth:
            self.little_bfs(self.get_start(), visited)
        else:
            self.little_dfs(self.get_start(), visited)
        for vertex in self.vertices:
            if vertex in visited or vertex.status is Status.OBSTACLE:
                continue
            if self.find == 0:
                return visited
            if breadth:
                self.little_bfs(vertex, visited)
            else:
                self.little_dfs(vertex, visited)
        print(self.find)
        return visited

    def get_start(self):
        return self.start

    def little_search(self, vertex, visited, breadth):
        """
        Use breadth first search on vertex and its neighbors.
        :param vertex: (Vertex) The start of the search.
        :param visited: (List of Vertex) Verticies that have alreaddy been visited.
        :param breadth: (Boolean) Use bfs if trues, use dfs otherwise
        :param find: (int) The number of targets left to find in self
        :return: The Verticies that were visited.
        """
        planned = collections.deque()
        planned.append(vertex)
        while len(planned) > 0 and self.find > 0:
            if breadth:
                current = planned.popleft()
            else:
                current = planned.pop()

            if current not in visited and (current.status is not Status.OBSTACLE):
                visited.append(current)
                if current.status is Status.TARGET:
                    self.find -= 1
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
        self.searching = False
        for vertex in self.vertices:
            if all or vertex.new_status is Status.NORMAL_VISITED:
                if vertex.status is Status.TARGET: self.targets.remove(vertex)
                elif vertex.status is Status.START: self.start = self.vertices[0]
                vertex.change_status(Status.NORMAL)
                vertex.h = MAX
                vertex.g = MAX


    def immediate_update(self):
        """
        Immediately update every vertex to switch to its appropriate status.
        :return: None
        """
        for vertex in self.vertices:
            vertex.delay = 0


class MyGrid(Graph):
    """An extension of Graph using inheritance. Grid represents a 2 by 2 grid as a connected graph"""
    def __init__(self, rows=30, cols=30):
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
        self.targets = set()

    def mutate(self, coordinate, status):
        """
        Mutate the vertex of the given coordinates to have the given status.
        :param coordinate: (Coordinate) The x and y value of the vertex to be mutated.
        :param status: (Status) A vertex can be NORMAL, TARGET or OBSTACLE.
        :return: None
        """
        mutate = self.vertex_by_coordinate.get(coordinate)
        if mutate is None:
            return
        if status is Status.TARGET:
            self.targets.add(mutate)
        elif mutate in self.targets: self.targets.remove(mutate)
        if status is Status.START:
            self.start.change_status(Status.NORMAL)
            self.start = mutate
        mutate.change_status(status)

    def a_star_algorithm(self):
        """Use the a* algorithm to find the target.
        Will stop if unfindable.
        g (int) the cost to travel to that cell
        h (double) the distance between this vector and the target
        """
        self.searching = True
        delay = 0
        open = dict()
        closed = []
        start = self.get_start()
        open.update({start : 0})
        start.g = 0
        for target in self.targets:
            while len(open) > 0:
                delay += 1
                current = self.get_closest(open)
                del open[current]
                closed.append(current)
                if current.get_status() is Status.NORMAL:
                    current.change_status(Status.NORMAL_VISITED, delay)
                elif current is target:
                    break
                for edge in current.edges:
                    neighbor = edge.neighbor
                    if neighbor.status is Status.OBSTACLE or neighbor in closed: continue
                    g = edge.distance
                    h = self.manhattan_distance(target, neighbor)
                    f = g + h
                    if f < open.get(neighbor, MAX) : open.update({neighbor : f})
        return closed





    def manhattan_distance(self, target, current):
        return math.sqrt((target.x - current.x)**2 + (target.y - current.y)**2)

    def get_closest(self, open):
        """

        :param open: (Dict)
        :return: (Vertex)
        """
        min = MAX
        for vertex, distance in open.items():
            if distance < min:
                min = distance
                closest = vertex
        return closest





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

    def __repr__(self):
        return "{name} {x} {y} {status}".format(name=self.name, x=self.x, y=self.y, status=self.new_status)

    def add_neighbor(self, neighbor):
        distance = random.randrange(MaxWeight)
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
    g.mutate(Coordinate(0, 5), Status.TARGET)