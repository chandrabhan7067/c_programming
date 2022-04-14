# 11. Find the path between given vertices in a directed graph.

class Graph:
 
    def __init__(self, edges, n):
 
        self.adjList = [[] for _ in range(n)]
 
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
def DFS(graph,s,d, visited,path):
 
    visited[s] = True
    path.append(s)
    if (s == d):
      print(path)
    else:  
      for u in graph.adjList[s]:
        if not visited[u]:
            DFS(graph, u,d, visited,path)
    path.pop()
    visited[s]= False
 
def path1(graph,n,s,d):
 
    visited = [False] * n
    path=[]
    
    DFS(graph,s, d,visited,path)
 
 
if __name__ == '__main__':
 
    edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
    print(edges)
    n = 5
 
    graph = Graph(edges, n)
    path1(graph,n,2,4)