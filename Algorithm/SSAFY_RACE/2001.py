T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill = 0
            try:
                for row in range(0, M):
                    for col in range(0, M):
                        kill += array[i+col][j+row]
                max_kill = max(max_kill, kill)
            except IndexError:
                continue
    print(f'#{tc} {max_kill}')