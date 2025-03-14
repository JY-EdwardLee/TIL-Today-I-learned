from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def get_dist(arr, p, N, M):
    i, j = p
    que = deque()
    Mu = []
    step = 0
    visited = []
    while True:
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and (ni,nj) not in visited:
                if arr[ni][nj] == "L":
                    Mu.append((ni, nj))
                    visited.append((ni, nj))
        if que:
            i, j = que.popleft()
        else:
            que.extend(Mu)
            Mu = []
            if que:
                i, j = que.popleft()
                step += 1
            else:
                return step
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                total += get_dist(arr, (i,j), N, M)
    # for row in arr_1:
    #     print(*row)
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