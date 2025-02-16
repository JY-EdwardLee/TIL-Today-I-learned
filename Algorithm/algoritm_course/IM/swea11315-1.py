import sys
sys.stdin = open("../input.txt", "r")


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

    # 대각선 판별하기
    for j in range(n): # 맨 윗쪽 행을 시작점으로 돌기
        omoki = 0
        i = 0
        # 행을 기준으로 출발점 오른쪽으로 이동
        while 0 <= i < n and 0 <= j < n:
            if arr[i][j] == 'o':
                omoki += 1
                if omoki == 5:
                    return "YES"
            elif arr[i][j] != 'o':
                omoki = 0
            i += 1
            j += 1
    for j in range(n): # 열을 기준으로 출발점 아래쪽으로 이동
        omoki = 0
        i = 0
        while 0 <= i < n and 0 <= j < n:
            if arr[j][i] == 'o':
                omoki += 1
                if omoki == 5:
                    return "YES"
            elif arr[j][i] != 'o':
                omoki = 0
            i += 1
            j += 1
        # 부대각선 판별
    for j in range(n): # 행을 기준으로 오른쪽으로 이동
        omoki = 0
        i = 0
        while 0 <= i < n and 0 <= j < n:
            if arr[i][j] == 'o':
                omoki += 1
                if omoki == 5:
                    return "YES"
            elif arr[i][j] != 'o':
                omoki = 0
            i += 1
            j -= 1
    for j in range(n): # 열을 기준으로 아래쪽으로 이동
        omoki = 0
        i = n - 1
        while 0 <= i < n and 0 <= j < n:
            if arr[j][i] == 'o':
                omoki += 1
                if omoki == 5:
                    return "YES"
            elif arr[j][i] != 'o':
                omoki = 0
            i -= 1
            j += 1
    return "NO"

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]
    print(f'#{tc} {omok(arr, N)}')
