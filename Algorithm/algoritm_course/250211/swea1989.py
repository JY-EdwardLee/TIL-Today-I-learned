import sys
sys.stdin = open('../input.txt', 'r')



T= int(input())


def wyw(N):
    if len(N) == 1:
        return N
    return N[-1] + wyw(N[:-1])


for tc in range(1, T+1):
    N = input().strip()
    print(f'#{tc} {int(N == wyw(N))}')
