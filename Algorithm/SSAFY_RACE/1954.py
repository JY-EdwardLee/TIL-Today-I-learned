# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    i = 1
    x = 0
    y = 0
    direction = 0
    while i <= N*N:
        snail[y][x] = i
        i += 1
        ny = y + dy[direction]
        nx = x + dx[direction]
        if 0 <= nx < N and 0 <= ny < N and snail[ny][nx] == 0:
            x = nx
            y = ny
        else:
            direction = (direction + 1)%4
            y = y + dy[direction]
            x = x + dx[direction]
    print(f'#{tc}')
    for line in snail:
        print(*line)