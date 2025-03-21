import heapq


def bfs(s, e):
    d = [float('inf')] * 1000001
    n = s
    d[n] = 0
    heap = []
    heapq.heappush(heap, (0, n))
    while True:
        cal, n = heapq.heappop(heap)
        if d[n] < cal:
            continue
        if n == e:
            return cal
        new_cal = cal + 1
        for j in cal_list:
            if j != 2 and 0 < n+j <= 1000000:
                if d[n+j] > new_cal:
                    d[n+j] = new_cal
                    heapq.heappush(heap, (new_cal, n+j))
            else:
                if 0 < n*j <= 1000000:
                    if d[n*j] > new_cal:
                        d[n*j] = new_cal
                        heapq.heappush(heap, (new_cal, n*j))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cal_list = [1, -1, 2, -10]
    print(f'#{tc} {bfs(N, M)}')