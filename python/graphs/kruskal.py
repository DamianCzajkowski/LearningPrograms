from .disjoint_set import DisjointSet as dst


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, sourve, destination, weight):
        for source, destination, weight in self.MST:
            print(f"{source} - {destination}: {weight}")

    def kruskal(self):
        i, e = 0
        ds = dst(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, w, d])
                ds.union(x, y)
        self.print_solution(s, d, w)
