import sys
sys.stdin = open("input.txt", "r")


T = int(input())

def typing(a, b):
    N = len(a)
    M = len(b)
    type_set = 0
    i = 0
    while i < N - M +1:
        if b == a[i:i+M]:
            type_set += M - 1
            i += M
        else:
            i += 1
    return N - type_set



for tc in range(1, T+1):
    A, B = map(str, input().split())
    print(f'#{tc} {typing(A, B)}')