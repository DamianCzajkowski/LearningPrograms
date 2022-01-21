from collections import defaultdict


class Graph:

    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        visited.append(v)

        for item in self.graph[v]:
            if item not in visited:
                self.topological_sort_util(item, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = []
        stack = []
        for key in list(self.graph):
            if key not in visited:
                self.topological_sort_util(key, visited, stack)
        print(stack)


custom_graph = Graph(8)
custom_graph.add_edge("A", "C")
custom_graph.add_edge("C", "E")
custom_graph.add_edge("E", "H")
custom_graph.add_edge("E", "F")
custom_graph.add_edge("F", "G")
custom_graph.add_edge("B", "D")
custom_graph.add_edge("B", "C")
custom_graph.add_edge("D", "F")

custom_graph.topological_sort()
