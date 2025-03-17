import sys
sys.stdin = open("../input.txt", "r")

from collections import deque

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    distance = [[-1] * M for _ in range(N)]  # 거리를 저장할 배열
    queue = deque()

    # 모든 W를 초기 위치로 큐에 삽입
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                queue.append((i, j))
                distance[i][j] = 0  # W의 위치는 거리 0

    # BFS 수행
    total = 0
    while queue:
        y, x = queue.popleft()
        for di, dj in delta:
            ni, nj = y + di, x + dj
            if 0 <= ni < N and 0 <= nj < M and distance[ni][nj] == -1:
                distance[ni][nj] = distance[y][x] + 1
                total += distance[ni][nj]  # 거리 합산
                queue.append((ni, nj))

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