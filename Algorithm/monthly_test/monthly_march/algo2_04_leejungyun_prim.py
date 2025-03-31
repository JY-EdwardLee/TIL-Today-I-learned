import heapq

# 두 콘센트의 거리를 구하는 함수
def get_dist(a, b):
    xi, yi = a
    xj, yj = b
    return abs(xi-xj) + abs(yi-yj)


# 콘센트 연결 함수
def link_all():
    global cal
    # 프림으로 풀기
    prim = []
    heapq.heappush(prim, (0, 0))
    total_dist = 0
    linked = [0] * (N+1)
    while 0 in linked:
        dist, e = heapq.heappop(prim)
        if linked[e] == 1:
            continue
        linked[e] = 1
        total_dist += dist
        for link_inf in adj_List[e]:
            if linked[link_inf[1]] != 1:
                heapq.heappush(prim, link_inf)
                cal += 1

    return total_dist



T = int(input())
for tc in range(1, T+1):
    cal = 0
    N = int(input())            # 콘센트 개수 N개
    consents = [(0, 0)]         # 콘센트의 위치정보를 담은 리스트 생성(인덱스가 콘센트 번호,누전차단기 위치는 미리 세팅)
    for i in range(1, N+1):     # 콘센트 정보를 입력 받아서 콘센트 위치정보 리스트에 삽입
        x, y = map(int, input().split())
        consents.append((x, y))
    # 거리 정보를 담은 콘센트 간의 인접 리스트 생성
    adj_List = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1, N+1):
            adj_List[i].append((get_dist(consents[i], consents[j]), j))
            adj_List[j].append((get_dist(consents[i], consents[j]), i))
    ans = link_all()
    print(f'#{tc} {ans}')
