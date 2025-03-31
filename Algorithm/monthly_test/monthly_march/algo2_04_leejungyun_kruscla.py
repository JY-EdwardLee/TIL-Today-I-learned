import heapq

# 두 콘센트의 거리를 구하는 함수
def get_dist(a, b):
    xi, yi = a
    xj, yj = b
    return abs(xi-xj) + abs(yi-yj)


# 콘센트 부모 찾기 함수
def find_set(a):
    if parents[a] == a:
        return a
    result = find_set(parents[a])
    parents[a] = result
    return parents[a]


# 두개의 콘센트 연결을 위한 union
def union(a, b):
    p_a = find_set(a)
    p_b = find_set(b)

    if p_a == p_b:
        return
    if p_a == 0:    # 콘센트가 누전 차단기에 연결 되어있는지 알아야 하기에
        parents[p_b] = p_a  # 누전차단기가 포함될 시 항상 누전차단기를 부모로
    else:
        parents[p_a] = p_b


# 콘센트 연결 함수
def link_all():
    global cal
    # 크루스칼을 ... 해야한다.
    heapq.heapify(adj_List) # 인접 리스트를 거리 순으로 최소힙으로 만들기
    total_dist = 0
    while sum(parents) != 0: # 모드 콘센트의 부모가 누전차단기가 될 때까지
        dist, a, b = heapq.heappop(adj_List)
        if find_set(a) == find_set(b): # 부모가 같으면 이미 연결되어 있음
            continue
        union(a, b) # 부모를 통일 시키기
        total_dist += dist  # 전체 거리 += 두 콘센트 간 거리
        for i in range(N+1): # 각 콘세트의 부모 업데이트
            find_set(i)
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
    adj_List = []
    for i in range(N):
        for j in range(i+1, N+1):
            adj_List.append((get_dist(consents[i], consents[j]), i, j))
    # 각 콘센트의 부모 노드 생성 (make_set)
    parents = [0]*(N+1)
    for i in range(N+1):
        parents[i] = i
    # 전체 연결하는 함수 동작
    ans = link_all()
    print(f'#{tc} {ans}')
