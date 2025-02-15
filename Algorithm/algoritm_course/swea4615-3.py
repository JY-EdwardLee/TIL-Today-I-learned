import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def change_arr(check, h, n):
    for r_position in range(h + 1, n):
        if check[r_position] == c:
            for i in range(h + 1, r_position):
                check[i] = c
            break
        if check[r_position] == 0:
            break
    for l_position in range(h - 1, -1, -1):
        if check[l_position] == c:
            for i in range(l_position, h):
                check[i] = c
            break
        if check[l_position] == 0:
            break

def othello(v, h, c, arr, n):
    # 체크리스트 생성
    check_list = []
    # v 행을 0~n-1 까지 리스트 형태로 추가
    check_list.append(arr[v])
    # h 열을 0~n-1 까지 리스트 형태로 추가
    sero_list = []
    for i in range(n):
        sero_list.append(arr[i][h])
    check_list.append(sero_list)
    # 델타 생성
    di = [1, -1, -1, 1]
    dj = [1, -1, 1, -1]
    # 대각선 vh를 기준으로 대각선으로 arr 숫자 채우기 (벗어난 범위는 -1으로 표기)
    cross_list = [-1]*n
    cross_list[h] = arr[v][h]
    cross_index = []
    for a, b in zip(di[:2], dj[:2]):
        for dist in range(1, n):
            ni = v + a*dist
            nj = h + b*dist
            if 0 <= ni < n and 0 <= nj < n:
                cross_list[nj] = arr[ni][nj]
                cross_index.append((ni,nj))
    check_list.append(cross_list)
    # 부대각선 vh를 기준으로 대각선으로 arr 숫자 채우기 (벗어난 범위는 -1으로 표기)
    incross_list = [-1]*n
    incross_list[h] = arr[v][h]
    incross_index = []
    for a, b in zip(di[2:], dj[2:]):
        for dist in range(1,n):
            ni = v + a*dist
            nj = h + b*dist
            if 0 <= ni < n and 0 <= nj < n:
                incross_list[nj] = arr[ni][nj]
                incross_index.append((ni,nj))
    check_list.append(incross_list)
    # 체크 리스트 점검 후 변경
    for check in check_list:
        if check != check_list[1]:
            change_arr(check, h, n)
        else:
            change_arr(check, v, n)
    # 가로
    arr[v] = check_list[0]
    # 세로
    for i in range(n):
        arr[i][h] = check_list[1][i]
    # 대각선
    for ni, nj in cross_index:
        if check_list[2][nj] != -1:
            arr[ni][nj] = check_list[2][nj]
    for ni, nj in incross_index:
        if check_list[3][nj] != -1:
            arr[ni][nj] = check_list[3][nj]

    return arr



for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    arr[N//2][N//2 - 1], arr[N//2 - 1][N//2] = 1, 1
    for _ in range(M):
        v, h, c = map(int, input().split())
        v -= 1
        h -= 1
        arr[v][h] = c
        othello(v, h, c, arr, N)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                white += 1
            elif arr[i][j] == 1:
                black += 1
    print(f'#{tc} {black} {white}')
