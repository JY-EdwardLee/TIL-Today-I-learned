di = [-1,0,1,0]
dj = [0,1,0,-1]

def check(i,j,d):        # 시작좌표, 방향
    x, y = i, j
    count = 0
    while True:
        st_i, st_j = -1, -1
        if matrix[x][y] == 0:
            matrix[x][y] += 2
            count += 1
        for k in [(d+3) % 4, (d+2) % 4, (d+1) % 4, d % 4]:
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                st_i, st_j, d = ni, nj, k
                break
        else:       # 2번 상황
            ni = x + di[(d+2) % 4]
            nj = y + dj[(d+2) % 4]
            if 0 <= ni < N and 0 <= nj < M:
                if matrix[ni][nj] == 1:  # 여기서 while 문 탈출?
                    break
                else:
                    st_i, st_j = ni, nj  # 후진 가능


        # count += 1
        x, y = st_i, st_j


    return count


N, M = map(int, input().split())
si, sj, direction = map(int, input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]
# print(matrix)


ans = check(si, sj, direction)

print(ans)

