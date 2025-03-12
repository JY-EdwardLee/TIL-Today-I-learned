import sys
sys.stdin = open("../input.txt", "r")


delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(arr, N):
    max_moving = 0
    result = []
    visited = []
    for y in range(N):
        for x in range(N):
            arr_1 = [[0]*N for _ in range(N)]
            i, j = y, x
            moving = 0
            while True:
                moving += 1
                for di, dj in delta:
                    ni = i + di
                    nj = j + dj
                    if 0 <= nj < N and 0 <= ni < N:
                        if arr[ni][nj] == arr[i][j] + 1:
                            if arr_1[ni][nj] != 0:
                                moving += arr_1[y][x]
                                break
                            arr_1[ni][nj] = arr_1[i][j] + 1
                            i, j = ni, nj
                            break
                else:
                    arr_1[y][x] = moving
                    break
            if max_moving < moving:
                result = (arr[y][x], moving)
                max_moving = moving
            elif max_moving == moving and result:
                if result[0] > arr[y][x]:
                    result = (arr[y][x], moving)
    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {" ".join(map(str, dfs(arr, N)))}')