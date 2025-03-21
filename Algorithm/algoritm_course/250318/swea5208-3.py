def dfs(idx, cnt, distance, subset):
    global min_change
    if distance >= N:
        min_change = min(min_change, cnt)
        return

    if cnt >= min_change:
        return

    if idx == N:
        return

    dfs(idx + 1, cnt + 1, distance + data[idx], subset + [data[idx]])
    dfs(idx + 1, cnt, distance, subset)


T = int(input())

for t in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]

    min_change = float('inf')
    dfs(1, -1, 0, [])
    print(f"#{t} {min_change}")
