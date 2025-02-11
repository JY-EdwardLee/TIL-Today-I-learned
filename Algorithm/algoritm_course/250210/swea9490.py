import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def baloon_pang(arr, n, m):
    # 방향 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    max_pang = 0
    for i in range(n):
        for j in range(m):
            total_pang = arr[i][j]
            for nx, ny in zip(dx, dy):
                for dist in range(1, arr[i][j]+1):
                    ni = i + ny*dist
                    nj = j + nx*dist
                    if 0 <= ni < n and 0 <= nj < m:
                        total_pang += arr[ni][nj]
            if max_pang < total_pang:
                max_pang = total_pang
    return max_pang


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {baloon_pang(arr, N, M)}')
