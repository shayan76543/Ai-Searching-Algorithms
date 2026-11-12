from collections import deque
class Graph:
    def __init__(self,vertexs):
        self.mat=[[0]*vertexs for i in range(vertexs)]
        self.vertexs=vertexs
        self.size=vertexs
    def add_edge(self,src,dist):
        if 0<=src<self.size and 0<=dist<self.size:
            self.mat[src][dist]=1
            self.mat[dist][src]=1
        else:
            print("Invalid edge")
    def BFS(self, src):
        visited = [False] * self.vertexs
        queue = deque([src]) # Parent node
        visited[src] = True          
        while queue:
            v = queue.popleft()
            print(v, end=" ")
            for i in range(self.size):
                if self.mat[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
g=Graph(9)
g.add_edge(5,8)
g.add_edge(5,3)
g.add_edge(8,6)
g.add_edge(8,2) 
g.add_edge(3,1)
g.add_edge(3,4)
g.BFS(5) #parent node
# Time and Space Complexity  T=> O(b**d) S=> O(b**d)