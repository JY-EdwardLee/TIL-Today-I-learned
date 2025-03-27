import sys
sys.stdin = open("../../input.txt", "r")

delta = [(1,0), (0,1), (-1,0), (0,-1)]

from collections import deque


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr_1 = [[0] * M for _ in range(N)]
    total = 0
    waters = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                waters.append((i,j))
    while True:
        # for i in range(N):
        #     for j in range(M):
        #         if arr[i][j] == "L":
        #             arr_1[i][j] += 1
        y, x = waters.popleft()
        for di, dj in delta:
            ni = y + di
            nj = x + dj
            if 0 <= y + di < N and 0 <= x + dj < M and arr[ni][nj] != "W":
                arr[y + di][x + dj] = "W"
                if arr_1[y + di][x + dj] == 0 or arr_1[y + di][x + dj] > arr_1[y][x] + 1:
                    arr_1[y + di][x + dj] = arr_1[y][x] + 1
                waters.append((y+di, x+dj))
        if not waters:
            break

    # for row in arr_1:
    #     print(*row)
    for row in arr_1:
        total += sum(row)
    print(f'#{tc} {total}')
'''
3
2 3
WLL
LLL
3 2
WL
LL
LW
4 5
LLLWW
WWLLL
LLLWL
LWLLL
'''