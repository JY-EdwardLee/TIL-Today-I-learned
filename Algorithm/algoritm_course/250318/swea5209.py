

def dfs(i, total):
    global min_total
    if total > min_total:
        return

    if i >= N:
        min_total = min(min_total, total)
        return

    for j in range(N):
        if j not in visited:
            visited.append(j)
            dfs(i+1, total + arr[i][j])
            visited.pop()


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_total = float('inf')
    visited = []
    dfs(0, 0)
    print(f'#{tc} {min_total}')