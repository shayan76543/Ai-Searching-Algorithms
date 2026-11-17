#  for Numbers Graph 
class Graph:
    def __init__(self, vertices):
        self.size = vertices
        self.mat = [[0] * vertices for i in range(vertices)]
    def add_edge(self, src, dest):
        self.mat[src][dest] = 1
        self.mat[dest][src] = 1
    def DLS(self, src, goal, limit):
        stack = [(src, 0)]
        visited = set()
        while stack:
            v, depth = stack.pop()
            if v in visited:
                continue
            visited.add(v)
            print(v, end="-->")
            if v == goal:
                return True
            if depth >= limit:
                continue
            for i in range(self.size):
                if self.mat[v][i] == 1 and i not in visited:
                    stack.append((i, depth + 1))
        return False
# Creating Graph
g = Graph(7)
# Adding Edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
# Calling DLS
result = g.DLS(0, 6, 2)
print("\nGoal Found:", result)
