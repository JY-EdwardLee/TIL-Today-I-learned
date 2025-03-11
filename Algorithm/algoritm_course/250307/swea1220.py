for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    deadlock = 0
    for j in range(N):
        flag = 0
        for i in range(N):
            if flag == 0:
                if arr[i][j] == 1:
                    flag = 1
                elif arr[i][j] == 2:
                    continue
            elif flag == 1:
                if arr[i][j] == 1:
                    continue
                elif arr[i][j] == 2:
                    flag = 0
                    deadlock += 1
    print(f'#{tc} {deadlock}')