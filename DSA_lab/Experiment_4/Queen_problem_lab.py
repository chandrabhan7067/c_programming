# 4. Print all possible solutions to N Queens problem.

N = int(input('Enter the size of board\n'))
board = [[0]*N for i in range(N)]


def is_attack(i, j):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    for m in range(0, N):
        for n in range(0, N):
            if (m+n == i+j) or (m-n == i-j):
                if board[m][n] == 1:
                    return True
    return False


def QUEEN(n):                   #here n is the number of Queen
    if n == 0:
        return True

    for i in range(0, N):
        for j in range(0, N):
            if (not(is_attack(i, j))) and (board[i][j] != 1):
                board[i][j] = 1

                if QUEEN(n-1) == True:
                    return True
                
                else:
                    board[i][j] = 0

    return False


QUEEN(N)
for i in board:
    print(i)


