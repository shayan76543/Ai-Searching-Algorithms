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

    def DFS(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                print(vertex, end=" --> ")
                visited.add(vertex)

                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)


g = Graph()

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

g.DFS(1)