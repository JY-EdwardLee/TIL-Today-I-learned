T = int(input())


def harvest(farm, n):
    amt_of_harvest = 0
    if n == 1:
        return farm[0][0]

    for i in range(n//2 + 1):
        wing = i
        amt_of_harvest += sum(farm[i][n//2-wing:n//2+wing+1])
    for i in range(n//2+1, n):
        wing = n - 1 - i
        amt_of_harvest += sum(farm[i][n//2-wing:n//2+wing+1])
    return amt_of_harvest

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {harvest(arr, N)}')