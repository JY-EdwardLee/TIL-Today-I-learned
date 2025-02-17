import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def othello(row, col, color, n, arr):
    row -= 1
    col -= 1
    arr[row][col] = color
    check_list = []
    # 가로 체크
    check_list.append(arr[row])
    # 세로
    sero_list = []
    for i in range(n):
        sero_list.append(arr[i][col])
    check_list.append(sero_list)
    di = [1, -1, -1, 1]
    dj = [1, -1, 1, -1]
    # 대각선
    cross_list = [arr[row][col]]
    for l, r in zip(di[:1], dj[:1]):
        for dist in range(1, n):
            ni = row + l*dist
            nj = col + r*dist
            if 0 <= ni < n and 0 <= nj <n:
                cross_list.append(arr[ni][nj])
    check_list.append(cross_list)
    # 부대각선
    incross_list = [arr[row][col]]
    for l, r in zip(di[2:], dj[2:]):
        for dist in range(1, n):
            ni = row + l*dist
            nj = col + r*dist
            if 0 <= ni < n and 0 <= nj <n:
                incross_list.append(arr[ni][nj])
    check_list.append(incross_list)
    print(check_list)






for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2 - 1][N//2 - 1] = (2, 2)
    arr[N//2][N//2 - 1], arr[N//2 - 1][N//2] = (1, 1)
    for _ in range(M):
        row, col, color = map(int, input().split())
        othello(row, col, color, N, arr)
    # print(f'#{tc} {black} {white}')