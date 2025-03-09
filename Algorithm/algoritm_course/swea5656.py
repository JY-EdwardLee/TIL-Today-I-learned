delta = [(0, -1), (1, 0), (0, 1)]


def bomb(y, x):
    for _ in range(3):
        for dist in range(int(arr[y][x])):
            ni = y + delta[i] * dist
            nj = x + delta[i] * dist
            if 0 <= ni < H and 0 <= ni < W:
                bomb(ni, nj)
    return

def crush(temp, N):
    for _ in range(N):
        j = temp.index(min(temp))
        if arr[i][j] == 0:
            continue
        else:
            bomb(i, j)
        temp[j] -= 1

    return



T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(input().split()) for _ in range(H)]
    bomb = []
    for j in range(W):
        temp = 0
        for i in range(H):
            if arr[i][j] == "1":
                temp += 1
            elif arr[i][j] not in ("0", "1"):
                bomb.append(temp)
                break
        else:
            bomb.append(temp)
    first_j = bomb.index(min(temp))
    crush(temp, N)
    total = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                total += 1
    print(f'#{tc} {total}')