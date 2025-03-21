import sys
import heapq
sys.stdin = open("../input.txt", "r")


def dijkstra(n):
    result = [float('inf')] * (n + 1)
    result[0] = 0
    for _ in range(E):
        heapq.heappush(heap, tuple(map(int, input().split())))
        if result[heap[0][0]] == float('inf'):
            continue
        s, e, c = heapq.heappop(heap)
        if result[e] < result[s] + c:
            continue
        result[e] = result[s] + c
    while heap:
        s, e, c = heapq.heappop(heap)
        if result[e] < result[s] + c:
            continue
        result[e] = result[s] + c
    return result[n]


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    heap = []
    print(f'#{tc} {dijkstra(N)}')
