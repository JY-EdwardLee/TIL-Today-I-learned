import sys
sys.stdin = open("algoritm_course/input.txt", "r")


T = int(input())


def max_balloon_pang(arr, n):
    # 방향 상 하 좌 우
    dy = [-1, 1, 0 ,0]
    dx = [0, 0, -1, 1]
    max_pang = 0
    for i in range(n):
        for j in range(n):
            pang = arr[i][j]
            for arrow in range(4):
                for dist in range(1, n):
                    ni = i + dy[arrow]*dist
                    nj = j + dx[arrow]*dist
                    if 0 <= ni < n and 0 <= nj < n:
                        pang += arr[ni][nj]
            max_pang = max(pang, max_pang)
    return max_pang

def min_balloon_pang(arr, n):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    min_pang = 9*n*n
    for i in range(n):
        for j in range(n):
            pang = arr[i][j]
            for arrow in range(4):
                for dist in range(1, n):
                    ni = i + dy[arrow] * dist
                    nj = j + dx[arrow] * dist
                    if 0 <= ni < n and 0 <= nj < n:
                        pang += arr[ni][nj]
            min_pang = min(pang, min_pang)
    return min_pang

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = max_balloon_pang(arr, N) - min_balloon_pang(arr, N)
    print(f'#{tc} {score}')