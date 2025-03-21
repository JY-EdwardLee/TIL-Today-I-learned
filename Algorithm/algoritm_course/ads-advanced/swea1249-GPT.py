import heapq

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dijkstra(arr, n):
    heap = []
    cnt = 0
    dist = [[float('inf')] * n for _ in range(n)]

    dist[0][0] = arr[0][0]
    heapq.heappush(heap, (arr[0][0], 0, 0))  # 시작점

    while heap:
        cost, i, j = heapq.heappop(heap)

        # 이미 더 짧은 거리로 방문된 경우라면 무시
        if dist[i][j] < cost:
            continue

        for di, dj in delta:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = cost + arr[ni][nj]
                if dist[ni][nj] > new_cost:
                    cnt += 1
                    dist[ni][nj] = new_cost
                    heapq.heappush(heap, (new_cost, ni, nj))

    return dist[n - 1][n - 1], cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]  # 숫자 붙어 있는 경우

    result = dijkstra(arr, N)
    print(f'#{tc} {result}')
