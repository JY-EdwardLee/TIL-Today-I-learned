import sys
sys.stdin = open("input.txt", "r")


def security(arr, p, M):
    y, x = p
    max_house = 0
    for dist in range(N+1):
        house = 0
        cost = (dist + 1)**2 + (dist)**2
        if max_House < cost:
            for i in range(y-dist, y+dist+1):
                for j in range(x-dist, x+dist+1):
                    if 0 <= i < N and 0 <= j < N:
                        if dist >= abs(i-y) + abs(j-x):
                            house += arr[i][j]
        if cost <= house*M:
            max_house = max(max_house, house)
    return max_house

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_House = 0
    for i in range(N):
        for j in range(N):
            House = security(arr, (i, j), M)
            max_House = max(max_House, House)
    print(f'#{tc} {max_House}')