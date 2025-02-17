import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def othello(row, col, color, n, arr):
    row -= 1
    col -= 1
    arr[row][col] = color
    # 세로 체크
    if (row + 1 < n):
        if arr[row+1][col] != 0:
            for i in range(row + 1, n):
                if arr[i][col] == color:
                    for change in range(row+1, i):
                        arr[change][col] = color
                    break       # for i
    if (0 <= row - 1):
        if arr[row-1][col] != 0:
            for i in range(row-1, -1, -1):
                if arr[i][col] == color:
                    for change in range(row-1, i, -1):
                        arr[change][col] = color
                    break       # for i
    # 가로 체크
    if (col + 1 < n):
        if arr[row][col+1] != 0:
            for j in range(col + 1, n):
                if arr[row][j] == color:
                    for change in range(col+1, j):
                        arr[row][change] = color
                    break       # for j
    if  (0 <= col - 1):
        if arr[row][col-1] != 0:
            for j in range(col - 1, -1, -1):
                if arr[row][j] == color:
                    for change in range(col-1, j, -1):
                        arr[row][change] = color
                    break       # for j
    # 대각선 체크
    if (row + 1< n) and (col + 1 < n):
        if arr[row+1][col+1] != 0:
            for i, j in zip(range(row+1, n), range(col+1,n)):
                if arr[i][j] == color:
                    for x, y in zip(range(row+1, i), range(col+1, j)):
                        arr[x][y] = color
                    break
    if (0 <= row - 1) and (0 <= col - 1):
        if arr[row-1][col-1] != 0:
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if arr[i][j] == color:
                    for x, y in zip(range(row-1, i, -1), range(col-1, j, -1)):
                        arr[x][y] = color
                    break
    # 부대각선 체크
    if (0 <= row - 1) and (col + 1 < n):
        if arr[row-1][col+1] != 0:
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if arr[i][j] == color:
                    for x, y in zip(range(row-1, i, -1), range(col+1, j)):
                        arr[x][y] = color
                    break
    if (row + 1 < n) and (0 <= col - 1):
        if arr[row+1][col-1] != 0:
            for i, j in zip(range(row+1, n), range(col-1, -1, -1)):
                if arr[i][j] == color:
                    for x, y in zip(range(row+1, i), range(col-1, j, -1)):
                        arr[x][y] = color
                    break


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2 - 1][N//2 - 1] = (2, 2)
    arr[N//2][N//2 - 1], arr[N//2 - 1][N//2] = (1, 1)
    for _ in range(M):
        row, col, color = map(int, input().split())
        othello(row, col, color, N, arr)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                white += 1
            elif arr[i][j] == 1:
                black += 1
    print(f'#{tc} {black} {white}')