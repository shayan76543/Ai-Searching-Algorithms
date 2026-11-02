from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def BFS(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            vertex = queue.popleft()

            print(vertex, end=" --> ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

g.BFS(1)