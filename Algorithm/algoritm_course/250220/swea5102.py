def bfs(v, g):
    que = []
    visited = [0]* (V + 1)
    lv = [0]* (V + 1)
    while True:
        for node in adj_list[v]:
            if visited[node] == 0:
                que.append(node)
                if lv[node] == 0:
                    lv[node] = lv[v] + 1
                if node == g:
                    return lv[node]
        else:
            if que:
                visited[v] = 1
                v = que.pop(0)
            else:
                return 0


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adj_list[v].append(w)
        adj_list[w].append(v)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, G)}')