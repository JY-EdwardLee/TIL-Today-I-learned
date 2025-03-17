import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find_space(puzzle, n, k):
    space_h, space_v = 0, 0     # 가로 세팅
    h = 0
    arr = [arr[:] for arr in puzzle]
    while h < n:
        # 가로 찾기
        for j in range(1, n):
            if arr[h][j] == 0:
                continue
            else:
                arr[h][j] += arr[h][j-1]
                if arr[h][j] == k:
                    space_h += 1
                elif arr[h][j] == k+1:
                    space_h -= 1
        # 세로 찾기
        for i in range(1, n):
            if puzzle[i][h] == 0:
                continue
            else:
                puzzle[i][h] += puzzle[i-1][h]
        for i in range(n):
            if puzzle[i][h] == k:
                space_v += 1
            elif puzzle[i][h] == k+1:
                space_v -= 1
        h += 1

    return space_v + space_h


for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {find_space(arr, N, K)}')
