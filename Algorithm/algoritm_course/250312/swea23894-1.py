import sys
sys.stdin = open("../input.txt", "r")

delta = [(1,0), (0,1)]

def brute(arr, N, p):
    i, j = p
    global cost
    global total
    if i == N-1 and j == N-1:
        total = min(total, cost)
        return
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            cost += arr[ni][nj]
            brute(arr, N, (ni, nj))
            cost -= arr[ni][nj]
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost = arr[0][0]
    total = float('inf')
    print(f'#{tc} {brute(arr, N, (0, 0))}')
