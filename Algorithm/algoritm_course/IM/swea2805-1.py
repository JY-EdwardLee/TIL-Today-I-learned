T = int(input())


def harvest(farm, n):
    center = n//2
    distance = n//2
    total_harvest = 0
    for i in range(n):
        for j in range(n):
            if distance >= abs(i - center) + abs(j - center):
                total_harvest += farm[i][j]
    return total_harvest

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {harvest(arr, N)}')