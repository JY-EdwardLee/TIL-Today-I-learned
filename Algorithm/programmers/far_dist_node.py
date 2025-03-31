from collections import deque

def solution(n, edge):
    adj_list = [[] for _ in range(n+1)]
    for link in edge:
        s, e = link
        adj_list[s].append(e)
        adj_list[e].append(s)
    visited = [0]*(n+1)
    visited[1] = 1
    dists = [0]*(n+1)
    que = deque()
    que.append(1)
    while que:
        s = que.popleft()
        for e in adj_list[s]:
            if not visited[e]:
                visited[e] = True
                dists[e] = dists[s] + 1
                que.append(e)
    max_dist = max(dists)
    return dists.count(max_dist)
n = 6
edge =[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))