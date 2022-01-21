import queue


class Graph:
    def __init__(self, gdict={}):
        self.gdict = gdict

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjancent_vertex in self.gdict[de_vertex]:
                if adjancent_vertex not in visited:
                    visited.append(adjancent_vertex)
                    queue.append(adjancent_vertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjancent_vertex in self.gdict[pop_vertex]:
                if adjancent_vertex not in visited:
                    visited.append(adjancent_vertex)
                    stack.append(adjancent_vertex)
