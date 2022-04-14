N = int(input("Enter the size of board\n"))
board = [[0]*4 for i in range(N)]

def is_attack(i,j):
    for k in range(N):
        if board[i][k] == 'Q' or board[k][j] == 'Q':
            return True

    for m in range(N):
        for n in range(N):
            if (m+n == i+j) or (m-n == i-j):
                if board[m][n] == 'Q':
                    return True
    return False


def Enter_Queen(size):
    if size == 0:
        return True

    for i in range(N):
        for j in range(N):
            if (not(is_attack(i,j))) and (board[i][j] != 1):
                board[i][j] = 'Q'

                if Enter_Queen(size-1) == True:
                    return True

                board[i][j] = 0

    return False

Enter_Queen(N)
for item in board:
    print(item)
