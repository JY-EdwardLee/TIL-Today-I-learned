from collections import deque
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(arr, n):
    que = deque()
    arr_17 = [[0]*n for _ in range(n)]
    i = j = 0
    while True:
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr_17[ni][nj] == 0 or arr_17[ni][nj] > arr_17[i][j] + arr[ni][nj]:
                    arr_17[ni][nj] = arr_17[i][j] + arr[ni][nj]
                    que.append((ni, nj))
        if que:
            i, j = que.popleft()
        else:
            break
    return arr_17[n-1][n-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {dijkstra(arr, N)}')