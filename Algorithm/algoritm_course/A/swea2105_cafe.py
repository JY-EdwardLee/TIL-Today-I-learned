
dy = [1, 1, -1, -1]
dx = [-1, 1, 1, -1]


def find_way(arr, position: tuple, N, d):
    y, x = position
    if d < 2:
        while True:
            cafe_list.append(arr[y][x])
            ny = y + dy[0]
            nx = x + dx[0]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] not in cafe_list:
                    y, x = ny, nx
                    square[d] += 1
                    find_way(arr, (y, x), N , d + 1)
                else:
                    break
            else:
                break

    if d == 3:
        for _ in range(square[0]):
            cafe_list.append(arr[y][x])
            ny = y + dy[0]
            nx = x + dx[0]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] not in cafe_list:
                    y, x = ny, nx
                else:
                    return
            else:
                return
        else:
            find_way(arr, (y, x), N, d + 1)
    if d == 4:
        for _ in range(square[1]):
            cafe_list.append(arr[y][x])
            ny = y + dy[0]
            nx = x + dx[0]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] not in cafe_list:
                    y, x = ny, nx
                else:
                    return
            else:
                return
        else:


T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if j == 0 or j == N-1:
                continue
            cafe_list = []
            square = [0] * 4
            find_way(arr, (i,j), N, 0)