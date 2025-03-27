

def dfs(i, success_rate):
    global max_rate
    if success_rate <= max_rate:
        return

    if i == N:
        max_rate = max(max_rate, success_rate)
        return

    for j in range(N):
        if j not in visited:
            visited.append(j)
            dfs(i + 1, success_rate * (arr[i][j]/100))
            visited.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(float, input().split())) for _ in range(N)]
    visited = []
    max_rate = 0
    dfs(0, 1)
    print(f"#{tc} {max_rate * 100:.6f}")