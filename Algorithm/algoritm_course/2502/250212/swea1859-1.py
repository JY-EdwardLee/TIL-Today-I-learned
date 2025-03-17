import sys
sys.stdin = open("../../input.txt", "r")


T = int(input())


def project_millionaire(arr, N):
    earned = 0
    max_price = arr[-1]
    for i in range(N-1, -1, -1):
        if arr[i] < max_price:
            earned += (max_price - arr[i])
        else:
            max_price = arr[i]

    return earned


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {project_millionaire(arr, N)}')
