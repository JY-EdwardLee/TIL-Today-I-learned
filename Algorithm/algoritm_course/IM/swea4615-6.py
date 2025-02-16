import sys
sys.stdin = open("../input.txt", "r")

T = int(input())

delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def switch_stone(delta_list, n, v, h, c):
    while (3 - c) in delta_list:    # 델타 인덱스에 다른 색이 있는지 확인
        stack = []  # 점검할 스택 생성
        valid = delta_list.index(3-c)  # 점검할 방향을 valid에 담기
        y, x = delta[valid]
        for dist in range(1, n):    # 보드판 끝까지 돌기
            ni = v + y * dist
            nj = h + x * dist
            if 0 <= ni < n and 0 <= nj < n:     # 좌표가 보드판 내부인지 점검
                if arr[ni][nj] == 3 - c:
                    stack.append((ni, nj))    # 다른 색 돌이 있으면 해당 좌표를 stack에 저장
                elif arr[ni][nj] == c:
                    if stack:      # 같은 돌을 만나면
                        for back_i, back_j in stack: # 스택에 저장된 좌표의 돌의 색깔을 변경
                            arr[back_i][back_j] = c
                        break
                    else:   # 스택이 비어 있으면 점검 종료
                        break  # for dist
                elif arr[ni][nj] == 0:
                    break
            else:   # 보드판 바깥이면 종료
                break       # for dist
        delta_list[valid] = 0  # 점검이 끝난 델타 인덱스는 0으로 처리

def othello(v, h, c, arr, n):
    v -= 1
    h -= 1
    arr[v][h] = c
    delta_list = [0] * 8
    for direction in range(len(delta)):  # 인접 영역 점검
        # 점검 방향을 i, j로 설정
        i , j = delta[direction]

        if v+i < 0 or v+i >= n or h+j < 0 or h+j >= n:  # 돌을 놓은 곳을 돌면서 해당 위치에 빈자리인지 검정돌인지 흰돌인지 delta_index에추가
            continue
        if arr[v+i][h+j] == 0:
            continue
        if arr[v+i][h+j] == 1:
            delta_list[direction] = 1
        if arr[v+i][h+j] == 2:
            delta_list[direction] = 2

    if c == 1: # 1(흑돌) 일 때
        switch_stone(delta_list, n, v, h, c)

    if c == 2: # 2(백돌) 일 때
        switch_stone(delta_list, n, v, h, c)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2, 2
    arr[N//2][N//2 - 1], arr[N//2 - 1][N//2] = 1, 1
    for _ in range(M):
        H, V, C = map(int, input().split())
        othello(V, H, C, arr, N)
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                white += 1
            elif arr[i][j] == 1:
                black += 1
    print(f'#{tc} {black} {white}')
