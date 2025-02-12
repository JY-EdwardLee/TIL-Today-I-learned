import sys
sys.stdin = open("../input.txt", "r")


T = int(input())

def typing(a, b):
    N = len(a)
    M = len(b)
    i = j = 0
    cnt = 0
    # A를 순회하면 B에 있는 문자열과 비교
    while i < N:
        x = a[i]
        if a[i] != b[j]:
            i = i - j + 1
            j = 0
            cnt += 1
        else:
            i += 1
            j += 1
        if j == M:
            j = 0
            cnt += 1
        if i == N and j != 0:
            cnt += j

    return cnt


for tc in range(1, T+1):
    A, B = map(str, input().split())
    print(f'#{tc} {typing(A, B)}')