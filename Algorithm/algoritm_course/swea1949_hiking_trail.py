T = int(input())
# 델타 : 하, 상, 우, 좌
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def is_lower(s, d, k):
    i, j = s
    visited.append(s)
    d += 1
    count = 0
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] < arr[i][j] and ((ni, nj) not in visited):
                count += 1
                able = (ni, nj)
                is_lower(able, d, k)
            elif arr[ni][nj] - k < arr[i][j] and ((ni, nj) not in visited):
                count += 1
                able = (ni, nj)
                temp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                is_lower(able, d, 0)
                arr[ni][nj] = temp
    if not count:
        global max_d
        max_d = max(max_d, d)
        visited.pop()
        return
    visited.pop()

for tc in range(1, T+1):
    N, K = map(int, input().split())
    max_height = 0  # 최대 높이
    arr = []
    dist = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        if max_height < max(temp):
            max_height = max(temp)
        arr.append(temp)
    start = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] == max_height:
                start.append((y, x))
    max_d = 0   # temp_max_dist
    for num in range(len(start)):
        visited = []
        is_lower(start[num], 0, K)
    print(f'#{tc} {max_d}')
