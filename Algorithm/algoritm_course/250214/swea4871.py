import sys
sys.stdin = open("../input.txt", "r")



def dfs(v, N, g):
    stack = []
    visited = [0] * (N+1)
    while True:
        if visited[v] == 0:
            visited[v] = 1
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    if visited[g] == 1:
        return 1
    else:
        return 0


for tc in range(1, 11):
    # 노드의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())
    # 간선을 저장할 경로 adj_list
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        v, w = map(int, input().split())
        adj_list[v].append(w)
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, V, G)}')