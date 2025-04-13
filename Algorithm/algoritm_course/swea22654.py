delta = [(-1,0), (0,1), (1, 0), (0, -1)]

T = int(input())

def find_rc():
    for y in range(N):
        for x in range(N):
            if mapk[y][x] == 'X':
                return y, x


def move_rc(a):
    global direction
    global x
    global y
    if a == 'A':
        dy, dx = delta[direction]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < N:
            if mapk[ny][nx] == 'T':
                return
            else:
                y, x = ny, nx
                return

    if a == 'R':
        direction += 1
        if direction > 3:
            direction = 0
        return
    if a == 'L':
        direction -= 1
        if direction < -3:
            direction = 0
        return


for tc in range(1, T+1):
    N = int(input())
    mapk_org = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []
    for _ in range(Q):
        count, action = input().split()
        direction = 0
        mapk = [mapk_org[w][:] for w in range(N)]
        y, x = find_rc()
        for i in range(int(count)):
            move_rc(action[i])
        if mapk[y][x] == 'Y':
            result.append(1)
        else:
            result.append(0)
    # print(f"#{tc}", *result)
    print(f"#{tc} {' '.join(map(str,result))}")
