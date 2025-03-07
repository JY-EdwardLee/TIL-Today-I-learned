dy = [1, 1, -1, -1]
dx = [-1, 1, 1, -1]


def walk(c_list, position: tuple, N, d):
    y, x = position
    c_list.append(arr[y][x])  # 방문한 카페 리스트 append
    ny = y + dy[d]
    nx = x + dx[d]
    if y == N and x == 0:  # 가장 모퉁이가면 어차피 못돌아서 break
        return False, False
    # 범위 안이고, 방문한 적 없으면
    if 0 <= ny < N and 0 <= nx < N \
            and arr[ny][nx] not in cafe_list \
            and arr[ny][nx] not in cafe_list_2 \
            and arr[ny][nx] not in cafe_list_1:
        square[d] += 1  # 해당 방향 이동 횟수 추가
        return ny, nx
    else:  # 범위 밖이거나, 방문한 적 있으면
        return False, False


def find_way(arr, position: tuple, N, d):
    y, x = position     # 입력 받은 출발지
    global way_to_cafe  # 최대 카페 방문 횟수
    if d == 0:  # 왼쪽 아래 탐색
        while True:
            y, x = walk(cafe_list, (y, x), N, d)
            if not y:
                cafe_list.clear()
                break
            find_way(arr, (y, x), N, d + 1)  # 방향 돌려서 다시 탐색

    if d == 1:
        while True:
            y, x = walk(cafe_list_1, (y, x), N, d)
            if not y:
                cafe_list_1.clear()
                square[d] = 0
                break
            find_way(arr, (y, x), N, d + 1)  # 방향 돌려서 다시 탐색

    if d == 2:
        if sum(square)*2 <= way_to_cafe:
            return
        for _ in range(square[0]):
            cafe_list_2.append(arr[y][x])
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N \
                    and arr[ny][nx] not in cafe_list \
                        and arr[ny][nx] not in cafe_list_2 \
                        and arr[ny][nx] not in cafe_list_1:
                    y, x = ny, nx
            else:
                cafe_list_2.clear()
                return
        else:
            find_way(arr, (y, x), N, d + 1)
            cafe_list_2.clear()
    if d == 3:
        if square[1] == 1:
            way_to_cafe = max(way_to_cafe, sum(square)*2)
            cafe_list_2.clear()
        else:
            for _ in range(square[1]-1):
                cafe_list_2.append(arr[y][x])
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[ny][nx] not in cafe_list \
                            and arr[ny][nx] not in cafe_list_2 \
                            and arr[ny][nx] not in cafe_list_1:
                        y, x = ny, nx
                    else:
                        cafe_list_2.clear()
                        return
                else:
                    cafe_list_2.clear()
                    return
            else:
                way_to_cafe = max(way_to_cafe, sum(square)*2)
                cafe_list_2.clear()

T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    way_to_cafe = -1    # 최대 카페 방문 횟수
    for i in range(N):
        for j in range(N):
            if j == 0 or j == N-1:  # 대각선 순회로 양 쪽 col은 검사 못함
                continue
            cafe_list = []      # ↙ 로 갈 때 카페 담을 리스트
            cafe_list_1 = []    # ↘로 갈 때 카페 담을 리스트
            cafe_list_2 = []    # ↗ ↖로 갈 때 카페 담을 리스트 (거리 및 내용이 정해져서 하나면 됨)
            square = [0] * 4    # 각 방향 별 이동 횟수
            find_way(arr, (i,j), N, 0)  # 최대 카페 방문 횟수
    print(f'#{tc} {way_to_cafe}')