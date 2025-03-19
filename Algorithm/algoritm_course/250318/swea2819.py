from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(p, nums):
    i, j = p
    if len(nums) == 7:
        set_list.add(nums)
        return

    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4 :
            dfs((ni, nj), nums + arr[ni][nj])


T = int(input())

for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    set_list = set()
    for y in range(4):
        for x in range(4):
            dfs((y, x), arr[y][x])
    print(f'#{tc} {len(set_list)}')
