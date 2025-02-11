import sys
sys.stdin = open("input.txt", "r")


T = int(input())


def snail(N):
    arr = [[0]*N for _ in range(N)]
    num = 0
    i = 0
    j = 0
    while i != N//2 or j != N//2:
        while j < N-1:
            num += 1
            if arr[i][j] == 0:
                arr[i][j] = num
                j += 1

        while i < N-1:
            num += 1
            if arr[i][j] == 0:
                arr[i][j] = num
                i += 1

        while 0 < j:
            num += 1
            if arr[i][j] == 0:
                arr[i][j] = num
                j -= 1

        while 1 < i:
            num +=1
            if arr[i][j] == 0:
                arr[i][j] = num
                i -= 1


for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc} {snail(N)}')