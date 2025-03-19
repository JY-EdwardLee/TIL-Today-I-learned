from collections import deque


def bfs(n, m):
    que = deque()
    que.append((m, 0))
    while True:
        m, cnt = que.popleft()
        if m == n:
            return cnt
        for cal in cal_list:
            if cal != 2 and 1 <= m + cal < 1000000:
                que.append((m + cal, cnt + 1))
            elif 1 <= m/cal < 1000000 and m%2 == 0:
                que.append((m//cal, cnt + 1))


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal_list = [-1, 1, 2, 10]
    print(f'#{tc} {bfs(N, M)}')