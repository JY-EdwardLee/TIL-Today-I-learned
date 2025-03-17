import sys
sys.stdin = open("../../input.txt", "r")

def dfs(adj_list, v, g):
    stack = []
    visited = [0] * 101
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
    num, M = map(int, input().split())
    graph = list(map(int, input().split()))
    arr_1 = [[] for _ in range(100)]
    arr_2 = [[] for _ in range(100)]
    adj_list = [[] for _ in range(100)]
    for i in range(M):
        v, w = graph[i*2], graph[i*2 + 1]
        if not arr_1[v]:
            arr_1[v] = w
        else:
            arr_2[v] = w
    for i in range(100):
        if arr_1[i]:
            adj_list[i].append(arr_1[i])
        if arr_2[i]:
            adj_list[i].append(arr_2[i])

    result = dfs(adj_list, 0, 99)
    print(f'#{tc} {result}')