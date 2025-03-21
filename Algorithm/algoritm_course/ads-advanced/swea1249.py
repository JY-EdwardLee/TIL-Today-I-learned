import heapq
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(arr, n):
    cnt = 0
    heap = []
    arr_17 = [[float('inf')]*n for _ in range(n)]
    i = j = 0
    flag, cost = 0, arr[0][0]
    while True:
        if arr_17[i][j] >= cost:
            arr_17[i][j] = cost
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if arr_17[ni][nj] > arr_17[i][j] + arr[ni][nj]:
                        arr_17[ni][nj] = cost + arr[ni][nj]
                        cnt += 1
                        heapq.heappush(heap, (arr_17[i][j] + arr[ni][nj], ni, nj))
        if heap:
            cost, i, j = heapq.heappop(heap)
            # if (i, j) == (n-1, n-1):
            #     return cost, cnt
        else:
            break
    return arr_17[n-1][n-1], cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {dijkstra(arr, N)}')