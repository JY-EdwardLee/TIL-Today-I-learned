delta = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(1, 11):
    tc = int(input())
    arr = []
    for _ in range(16):
        x = list(map(int, input()))
        arr.append(x)
        if 2 in set(x):
            i, j = _, x.index(2)
    visited = []
    que = []
    while True:
        visited.append((i, j))
        for di, dj in delta:
            ni = i +di
            nj = j +dj
            if 0 <= ni < 16 and 0 <= nj < 16:
                if arr[ni][nj] == 0 and (ni, nj) not in visited:
                   que.append((ni, nj))
                elif arr[ni][nj] == 3:
                    print(f'#{tc} {1}')
                    break
        else:
            if que:
                i, j = que.pop(0)
            else:
                print(f'#{tc} {0}')
                break
        if arr[ni][nj] == 3:
            break
