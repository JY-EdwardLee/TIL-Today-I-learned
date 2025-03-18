import sys
sys.stdin = open("../input.txt", "r")

from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_dist(arr, p, N, M):
    y, x = p
    i, j = p
    que = deque()
    Mu = []
    while True:
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if abs(y - i) + abs(x - j) > 1 and arr[ni][nj] == "W":
                    return
                if arr[ni][nj] == "L":
                    if arr_1[ni][nj] == 0 or arr_1[ni][nj] > abs(y - ni) + abs(x - nj):
                        Mu.append( (ni, nj))
                        arr_1[ni][nj] = abs(y - ni) + abs(x - nj)
        if que:
            i, j = que.popleft()
        else:
            que.extend(Mu)
            Mu = []
            if que:
                i, j = que.popleft()
            else:
                return
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    total = 0
    arr_1 = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                get_dist(arr, (i,j), N, M)
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