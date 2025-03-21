from collections import deque


def bfs(n, m):
    d = [0] * 1000001
    que = deque()
    que.append(n)
    while True:
        n = que.popleft()
        if n == m:
            return d[n]
        for j in cal_list:
            if j != 2 and 0 < n+j <= 1000000:
                if d[n+j] == 0 or d[n+j] > d[n] + 1:
                    que.append(n + j)
                    d[n+j] = d[n] + 1
            else:
                if 0 < n*j <= 1000000:
                    if d[n*j] == 0 or d[n*j] > d[n] + 1:
                        que.append(n * j)
                        d[n*j] = d[n] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal_list = [1, -1, 2, -10]
    print(f'#{tc} {bfs(N, M)}')