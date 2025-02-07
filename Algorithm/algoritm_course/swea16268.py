import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def balloon_pang(n, m):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 방향 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    total_pang = 0
    for i in range(n):
        for j in range(m):
            pang = arr[i][j]
            for direction in range(4):
                ni = i + di[direction]
                nj = j + dj[direction]
                if 0 <= ni < n and 0 <= nj < m:
                    pang += arr[ni][nj]
            if total_pang < pang:
                total_pang = pang
    return total_pang


for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {balloon_pang(N, M)}')
