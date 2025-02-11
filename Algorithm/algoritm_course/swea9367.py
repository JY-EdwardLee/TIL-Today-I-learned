import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def carrot_market(n, c):
    cre = 1
    max_cre = 1
    for i in range(n-1):
        if c[i] < c[i+1]:
            cre += 1
            max_cre = max(cre, max_cre)
        else:
            cre = 1
    return max_cre


for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    print(f'#{tc} {carrot_market(N, C)}')
