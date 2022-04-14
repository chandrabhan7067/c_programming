# 7. Check if a graph is strongly connected or not.

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[]for i in range(n)]

        for src, dest in edges:
            self.adjList[src].append(dest)


def DFS(Grapgh, v, visited):
    visited[v] = True

    for u in Grapgh.adjList[v]:
        if not visited[u]:
            DFS(Grapgh, u, visited)


def StronglyConnected(graph, n):
    for i in range(n):
        visited = [False]*n

        DFS(graph, i, visited)

        for b in visited:
            if not b:
                return False

    return True


if __name__ == '__main__':
    edges = [(0, 4), (1, 0), (1, 2), (2, 1), (2, 4), (3, 1), (3, 2), (4, 3)]
    n = 5
    graph = Graph(edges, n)

    if StronglyConnected(graph, n):
        print('The graph is strongly connected')
    else:
        print('The graph is not strongly connected')
