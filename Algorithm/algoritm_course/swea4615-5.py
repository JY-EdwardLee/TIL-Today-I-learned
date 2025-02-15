import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def othello(v, h, c, arr, n):
    v -= 1
    h -= 1
    arr[v][h] = c
    # 체크리스트 생성
    check_list = []
    # 가로
    check_list.append(arr[v])
    # 세로
    sero_list = []
    for i in range(n):
        sero_list.append(arr[i][h])
    check_list.append(sero_list)
    # 델타 생성
    di = [1, -1, -1, 1]
    dj = [1, -1, 1, -1]
    # 대각선
    cross_list = [0]*n
    cross_list[h] = arr[v][h]
    for a, b in zip(di[:2], dj[:2]):
        for dist in range(1, n):
            ni = v + a*dist
            nj = h + b*dist
            if 0 <= ni < n and 0 <= nj < n:
                cross_list[nj] = arr[ni][nj]
    check_list.append(cross_list)
    # 부대각선
    incross_list = [0]*n
    incross_list[h] = arr[v][h]
    for a, b in zip(di[2:], dj[2:]):
        for dist in range(1,n):
            ni = v + a+dist
            nj = h + b*dist
            if 0 <= ni < n and 0 <= nj < n:
                incross_list[nj] = arr[ni][nj]
    check_list.append(incross_list)
    # 체크 리스트 점검 후 변경
    for check in check_list:






    # 가로
    arr[v] = check_list[0]
    # 세로
    for i in range(n):
        arr[i][h] = check_list[1][i]
    # 대각선
    for a, b in zip(di[:2], dj[:2]):
        for dist in range(1, n):
            ni = v + a * dist
            nj = h + b * dist
            if 0 <= ni < n and 0 <= nj < n:
                arr[ni][nj] = check_list[2][nj]
    check_list.append(cross_list)
    # 부대각선
    for a, b in zip(di[2:], dj[2:]):
        for dist in range(1, n):
            ni = v + a + dist
            nj = h + b * dist
            if 0 <= ni < n and 0 <= nj < n:
                arr[ni][nj] = check_list[3][nj]

    return arr



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    arr[N//2][N//2 - 1], arr[N//2 - 1][N//2] = 1, 1
    for _ in range(M):
        v, h, c = map(int, input().split())
        othello(v, h, c, arr, N)
