import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 델타 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def is_exit(arr, n):
    stack = []
    visited = []
    # 출발점 탐색
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 2:
                i, j = y, x
                break
    while True:
        for di, dj in zip(dy, dx):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if (ni, nj) in stack:
                    continue
                if (ni, nj) in visited:
                    continue
                if arr[ni][nj] == 3:
                    return 1
                if arr[ni][nj] == 0:
                    stack.append((i, j))
                    i, j = ni, nj
                    visited.append((ni, nj))
                    break
        else:
            if stack:
                i, j = stack.pop()
            else:
                break
    return 0


for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {is_exit(arr, N)}')

