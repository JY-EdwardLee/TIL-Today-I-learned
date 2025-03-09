from collections import deque

# 델타 : 북, 서, 남, 동
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check = [2, 3, 0, 1]

pipe = {
    "1": (0, 1, 2, 3),
    "2": (0, 2),
    "3": (1, 3),
    "4": (0, 3),
    "5": (2, 3),
    "6": (1, 2),
    "7": (0, 1),
}


def bfs():
    ably = []
    while able:
        r, c = able.pop(0)
        for i in pipe[arr[r][c]]:
            dr, dc = delta[i]
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == "0" or (nr, nc) in move:
                    continue
                if check[i] in pipe[arr[nr][nc]]:
                    if (nr, nc) not in ably:
                        ably.append((nr, nc))
    return ably

T = int(input())

for tc in range(1, T+1):
    # position = R, C
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(N)]
    time = 1
    move = [(R, C)]
    able = [(R, C)]
    while time != L:
        able = bfs()
        move.extend(able)
        time += 1
    print(f'#{tc} {len(move)}')