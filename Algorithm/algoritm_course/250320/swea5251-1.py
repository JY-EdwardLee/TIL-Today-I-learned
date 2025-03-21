import heapq

def dijkstra(start):
    n = len(MAP) # 노드의 개수
    # result 배열은 양의 무한대로 초기화
    result = [float('inf')] * n
    # 시작노드
    result[start] = 0
    # 우선순위 큐 초기화(시작지점)
    pq = [(0, start)] # 0:비용, start:노드

    # 우선순위 큐가 빌때까지 반복
    while pq:
        # 다익스트라 1단계. 힙에서 뺀다(탐색) : 최소힙
        price, now = heapq.heappop(pq)

        if result[now] < price: continue # 비용이 result배열의 값보다 크면 continue

        # 다익스트라 2단계. 다음 갈 곳 예약걸기(큐 등록)
        for i in range(n):
            if MAP[now][i] == 0: continue
            next_price = MAP[now][i] # 인접행렬의 가중치
            price_sum = price + next_price # 누적합
            if result[i] > price_sum: # 최소 비용 갱신
                result[i] = price_sum
                heapq.heappush(pq, (price_sum, i)) # (비용, 노드)

    return result # result배열 반환

T = int(input())
for tc in range(1, T + 1):
    # N은 노드(N+1개), E는 간선
    N, E = map(int, input().split())
    MAP = [[0] * (N+1) for _ in range(N + 1)]

    for _ in range(E):
        start, end, weight = map(int, input().split())
        MAP[start][end] = weight

    result = dijkstra(0)
    print(f'#{tc} {result[N]}')