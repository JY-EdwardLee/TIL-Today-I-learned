# BFS는 선입선출(큐)
# from collections import deque

# 다익스트라는 최소힙(우선순위 큐)
import heapq

MAP = [[0] * 6 for _ in range(6)]

MAP[0][1] = 15
MAP[0][3] = 22
MAP[1][2] = 5
MAP[2][3] = 6
MAP[2][4] = 2
MAP[3][5] = 7
MAP[4][5] = 1

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

# start node는 0
result = dijkstra(0)
print(*result)