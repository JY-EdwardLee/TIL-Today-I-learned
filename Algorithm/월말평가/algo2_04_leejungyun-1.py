# 델타 : 상, 하, 좌, 우
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_dist(i, j):
    arr_1 = [[0]*N for _ in range(N)] # 자취 점검을 위한 arr 복사본
    visited = [(i, j)]      # 방문
    que = []      # 걸어온 길 기록을 위한 stack
    step = 1        # 거리
    arr_1[i][j] = 1
    while True:
        for di, dj in delta:
            if arr[i][j] == 4:
                di, dj = di*2, dj*2
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
                if arr[ni][nj] == 1:
                    continue
                elif arr[ni][nj] == 0 or arr[ni][nj] == 4:
                    arr_1[ni][nj] = arr_1[i][j] + 1
                    que.append((ni, nj))
                elif arr[ni][nj] == 3:
                    return (arr_1[i][j] + 1)
        if que:
            i, j = que.pop(0)
            step += 1
            visited.append((i, j))
        else:
            return -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 출발점 찾기
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                si, sj = y, x
                break

    print(f'#{tc} {get_dist(si, sj)}')