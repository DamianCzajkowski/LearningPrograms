class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex distance from source")
        for key, value in dist.items():
            print(' '+key, ' :  ', value)

    def bellman_ford(self, source):
        dist = {i: float("Inf") for i in self.nodes}
        dist[source] = 0

        for _ in range(self.V - 1):
            for source, destination, weight in self.graph:
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    dist[destination] = dist[source] + weight

        for source, destination, weight in self.graph:
            if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                print("Graph contains negative cycle")

        self.print_solution(dist)
