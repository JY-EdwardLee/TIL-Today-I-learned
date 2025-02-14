import sys
sys.stdin = open("input.txt", "r")


T = int(input())


def omok(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 'o':
                break
        else:
            return 'YES'
        for j in range(n):
            if arr[j][i] != 'o':
                break
        else:
            return 'YES'
    for i in range(n):
        if arr[i][i] != 'o':
            break
    else:
        return 'YES'
    for i in range(n):
        if arr[n-1-i][i] != 'o':
            break
    else:
        return 'YES'
    return 'NO'



for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(5)]
    print(f'#{tc} {omok(arr, N)}')
