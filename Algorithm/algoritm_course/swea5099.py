from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizzarin = list(map(int, input().split()))
    firefit = deque([0]*N)
    i = 1
    result = []
    while True:
        if firefit[0] == 0 and i <= M:
            firefit[0] = i
            i += 1
        elif firefit[0] !=0:
            pizzarin[firefit[0] - 1] = pizzarin[firefit[0] - 1]//2
            if pizzarin[firefit[0] - 1] == 0:
                result.append(firefit[0])
                firefit[0] = 0
        if firefit[0] == 0 and i <= M:
            firefit[0] = i
            i +=1
        firefit.rotate(1)
        if len(result) == M:
            break
    print(f'#{tc} {result[-1]}')