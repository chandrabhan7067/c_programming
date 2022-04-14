def Dijkstras_ALgo(G):
    n = len(G)
    k = 1
    for i in range(n):
        for j in range(n):
            G[i][j] = min(G[i][j],G[i][k] + G[k][i])
    print_Graph(G)

def print_Graph(distance):
    n = len(distance)
    for i in range(n):
        for j in range(n):
            if distance[i][j] == INF:
                print('INF',end=' ')
            else:
                print(distance[i][j],end=' ')
        print(' ')

INF = 1089
G = [[0, 3, INF, 7],
         [8, 0, 2,INF],
         [5, INF, 0, 1],
         [2, INF, INF, 0]]
Dijkstras_ALgo(G)
