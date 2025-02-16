import sys
sys.stdin = open("../input.txt", "r")

dy = [-1, 1, -1, 1]
dx = [-1, 1, 1, -1]


def change_check(line, start, n, color):
    for r_position in range(start + 1, n):
        if line[r_position] == 0 or line[r_position] == -1:
            break   # for r_position
        elif line[r_position] == color:
            for i in range(start + 1, r_position):
                line[i] = color
            break   # for r_position
    for l_position in range(start - 1, -1, -1):
        if line[l_position] == 0 or line[l_position] == -1:
            break   # for l_position
        elif line[l_position] == color:
            for i in range(start - 1, l_position, -1):
                line[i] = color
            break   # for l_position


def othello(x, y, board, n, c):
    # 체크 리스트 생성
    check_list = [[0] for _ in range(4)]
    # y행 추가
    check_list[0] = board[y]
    # x열 추가
    x_line = []
    for i in range(n):
        x_line.append(board[i][x])
    check_list[1] = x_line
    # 대각선 추가
    cross_line = [-1] * n
    cross_line[x] = board[y][x]
    cross_index = []
    for di, dj in zip(dy[:2], dx[:2]):
        for dist in range(1, n):
            ni = y + (di * dist)
            nj = x + (dj * dist)
            if 0 <= ni < n and 0 <= nj < n:
                cross_line[nj] = board[ni][nj]
                cross_index.append((ni, nj))
    check_list[2] = cross_line
    # 부대각선 추가
    subcross_line = [-1] * n
    subcross_line[x] = board[y][x]
    subcross_index = []
    for di, dj in zip(dy[2:], dx[2:]):
        for dist in range(1, n):
            ni = y + (di * dist)
            nj = x + (dj * dist)
            if 0 <= ni < n and 0 <= nj < n:
                subcross_line[nj] = board[ni][nj]
                subcross_index.append((ni, nj))
    check_list[3] = subcross_line
    # 체크 리스트 점검 후 변경
    for line in check_list:
        if line != check_list[1]:
            change_check(line, x, n, c)
        else:
            change_check(line, y, n, c)

    # 변경사항 적용
    # 가로
    board[y] = check_list[0]
    # 세로
    for i in range(n):
        board[i][x] = check_list[1][i]
    # 대각선
    for ni, nj in cross_index:
        board[ni][nj] = check_list[2][nj]
    for ni, nj in subcross_index:
        board[ni][nj] = check_list[3][nj]

T = int(input())
for tc in range(1, T+1):
    # 한 변의 길이 B, 돌을 놓는 횟수 M
    N, M = map(int, input().split())
    # 보드판 생성
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2] = board[N//2-1][N//2-1] = 2
    board[N//2][N//2 - 1] = board[N//2 - 1][N//2] = 1
    for _ in range(M):
        X, Y, C = map(int, input().split())
        X -= 1
        Y -= 1
        board[Y][X] = C
        othello(X, Y, board, N, C)
    white = black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print(f'#{tc} {black} {white}')