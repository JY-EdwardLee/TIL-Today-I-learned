delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def make_num(arr, p, move, num):
    i, j = p
    if move == 6:
        if num not in num_list:
            num_list.append(num)
        return
    for di, dj in delta:
        ni = i + di
        nj = j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            make_num(arr, (ni, nj), move + 1, num + arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [(list(map(str, input().split()))) for _ in range(4)]
    num_list = []
    for i in range(4):
        for j in range(4):
            make_num(arr, (i, j), 0, arr[i][j])
    print(f'#{tc} {len(num_list)}')