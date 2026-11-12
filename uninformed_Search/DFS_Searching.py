class Graph:
    def __init__(self,vertexs):
        self.mat=[[0]*vertexs for i in range(vertexs)]
        self.vertexs=vertexs
        self.size=vertexs
    def add_edge(self,src,dest):
        if 0<=src<self.vertexs and 0<=dest<self.vertexs:
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("Invalid Edge")
    def print_edge(self):  
        for row in self.mat:
            print(" ".join(map(str,row)))                
    def DFS(self, src):
        visited = [False] * self.vertexs
        stack = [src]
        visited[src] = True
        while stack:
            v = stack.pop()
            print(v, end="-->")
            for i in range(self.size):
                if self.mat[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    stack.append(i)
g=Graph(6)
g.add_edge(2,1)
g.add_edge(2,4)
g.add_edge(4,5)
g.print_edge()
g.DFS(1)
# Time Compexity and Space Complexity Time Com->O(b**m)  Space Com ->O(bd)