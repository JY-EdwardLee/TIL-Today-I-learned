from collections import deque


def bfs(n, m):
    d = [0] * 999999
    cnt = 0
    for i in range(n, 1000000):
        cnt += 1
        if i == m:
            return d[i]
        for j in cal_list:
            if j != 2 and 0 < i+j < 1000000:
                if d[i+j] == 0:
                    d[i+j] = d[i] + 1
            else:
                if 0 < i*j < 1000000:
                    if d[i+j] == 0:
                        d[i*j] = d[i] + 1


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal_list = [1, -1, 2, -10]
    print(f'#{tc} {bfs(N, M)}')