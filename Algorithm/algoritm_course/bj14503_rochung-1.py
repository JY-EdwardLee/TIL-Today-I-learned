N, M = map(int, input().split())
# 북동남서 (0123)
r, c, d = map(int, input().split())
# 0 청소 x, 1 청소 o
arr = [list(map(int, input().split())) for _ in range(N)]

# 방위
direction = [3, 0, 1, 2]
forward = [2, 3, 0, 1]
# 델타 북(0) 동(1) 남(2) 서(3)
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

count = 0
while True:
    if arr[r][c] == 0:
        count += 1
        arr[r][c] = 'c'
    for _ in range(4):
        d = direction[d]
        ni = r + dy[forward[d]]
        nj = c + dx[forward[d]]
        try:
            if arr[ni][nj] == 'c' or arr[ni][nj] == 1:  # 벽이거나 청소했으면
                continue
            elif arr[ni][nj] == 0:
                r = ni
                c = nj
                break  # for di, dj
        except IndexError:
            continue
    else:   # 청소할 곳 없을 때
        # 후진 try
        ni = r + dy[d]
        nj = c + dx[d]
        try:
            if arr[ni][nj] == 1:    # 벽이면
                break   # while true
            else:   # 아니면
                r = ni
                c = nj
        except IndexError:
            break
print(count)
