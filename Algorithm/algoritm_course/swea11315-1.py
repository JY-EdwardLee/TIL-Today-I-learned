import sys
sys.stdin = open("input.txt", "r")


T = int(input())


def omok(arr, n):
    for i in range(n):
        omoki = 0
        for j in range(n):
            if arr[i][j] == 'o':
                omoki += 1
                if omoki == 5:
                    return "YES"
            elif arr[i][j] != 'o':
                omoki = 0
        omoki = 0
        for j in range(n):
            if arr[j][i] == 'o':
                omoki += 1
                if omoki ==5:
                    return "YES"
            elif arr[j][i] != 'o':
                omoki = 0
    for i in range(n):
        omoki = 0
        if arr[i][i] == 'o':
            omoki += 1
            if omoki ==5:
                return "YES"
        elif arr[i][i] != 'o':
            omoki = 0
    for i in range(n):
        if arr[n-1-i][i] == 'o':
            omoki += 1
            if omoki ==5:
                return "YES"
        elif arr[n-1-i][i] != 'o':
            omoki = 0
    return 'NO'



for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(5)]
    print(f'#{tc} {omok(arr, N)}')
