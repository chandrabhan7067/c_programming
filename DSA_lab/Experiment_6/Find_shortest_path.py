# 6. All-Pairs Shortest Paths – Floyd Warshall Algorithm.

def floyd_warshall(G):
    n = len(G)
    # Adding vertices individually
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    print_solution(G)

def print_solution(distance):
    n = len(distance)
    for i in range(n):
        for j in range(n):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")
        
INF = 1089
G = [[0, 3, INF, 7],
         [8, 0, 2,INF],
         [5, INF, 0, 1],
         [2, INF, INF, 0]]

# G = [[0,   5,  INF, 10],
#     [INF,  0,  3,  INF],
#     [INF, INF, 0,   1],
#     [INF, INF, INF, 0]]

floyd_warshall(G)

