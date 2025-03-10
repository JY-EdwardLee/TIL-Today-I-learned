import sys
sys.stdin = open("input.txt", "r")

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def crush(y, x):
    if (y, x) not in destroy:
        destroy.append((y, x))
    for dy, dx in delta:    # 델타
        for dist in range(1, arr[y][x]):    # 벽돌에 써진 범위 만큼
            ny = y + dy*dist
            nx = x + dx*dist
            if 0 <= ny < H and 0 <= nx < W:   # 범위 안이면
                if arr[ny][nx]: # 0이 아니면
                    if (ny, nx) not in destroy: # 파괴 목록에 없으면
                        destroy.append((ny, nx)) # 추가
                        if arr[ny][nx] > 1:
                            crush(ny, nx)  # 또 깨기
    return len(destroy), destroy

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # N 범위 안에 2 이상의 벽돌 있는지 확인
    while N != 0:
        max_amount = 0  # 젤 많이 깨는게 뭔지 확인
        amount = 0
        max_temp = 0
        for i in range(W):  # 넓이 만큼
            arr_copy = list(zip(*arr))[::-1]    # for문 돌리기 편하게 눞히기
            temp = 0    # 돌던지기 횟수, 그리고 마지막에 깨진 벽돌 추가하기
            if tuple(set(arr_copy[i])) not in (0, 1, (0, 1)):   # 0 또는 1로 이루어진 벽돌이 아니면
                destroy = []
                for k in range(H):
                    if arr_copy[i][k]:  # 0이 아니면
                        destroy.append((k, W - i - 1))
                        temp += 1  # 벽돌 깨진 거니까 던진 것
                    if arr_copy[i][k] != 0 and arr_copy[i][k] != 1:  # 2 이상이면
                        amount, destroy = crush(k, W - i - 1)  # 얼마나 깰 수 있는 지 테스트
                        break
                    if temp == N:  # 던지기 횟수 다되면
                        break  # 그만 두기
                if max_amount < amount:
                    max_amount = amount
                    max_temp = temp
                    destroy_bricks = destroy
        for y, x in destroy_bricks:     # 진짜 깨버리기
            arr[y][x] = 0
        arr_2 = [[0]*W for _ in range(H)]
        for j in range(W):
            h = H - 1
            for i in range(H-1, 0, -1):
                if arr[i][j] != 0:
                    arr_2[h][j] = arr[i][j]
                    h -= 1
        arr = arr_2
        N -= max_temp   # 깬 횟수만큼 차감
    result = 0
    for l in range(H):
        for m in range(W):
            if arr[l][m] != 0:
                result += 1
    print(f'#{tc} {result}')