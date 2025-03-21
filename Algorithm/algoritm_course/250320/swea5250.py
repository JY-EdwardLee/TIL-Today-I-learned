import heapq
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(arr, n):
    heap = []
    heapq.heappush(heap, (0, 0, 0))
    arr_1 = [[float('inf')] * n for _ in range(n)]
    while heap:
        cost, i, j = heapq.heappop(heap)
        if arr_1[i][j] < cost:
            continue
        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = cost + 1 + (arr[ni][nj] - arr[i][j] if arr[ni][nj] - arr[i][j] > 0 else 0)
                if new_cost < arr_1[ni][nj]:
                    arr_1[ni][nj] = new_cost
                    heapq.heappush(heap, (new_cost, ni, nj))
    return arr_1[n-1][n-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra(arr, N)}')