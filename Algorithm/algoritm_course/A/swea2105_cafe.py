from collections import deque
# 델타 정방향
delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def get_line_sum(i, j, d):
    stack = []
    visited = []
    if d == 2:
        for _ in range(((i - I) + (J-j))/2):
            menu_list.append(arr[i][j])
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if arr[ni][nj] not in menu_list:
                stack.append((i, j))
                i, j = ni, nj
                visited.append((i, j))
            else:
                return -1
        else:
            get_line_sum(i, j, d+1)
            return
    if d == 3:
        while i != I and j != J:
            menu_list.append(arr[i][j])
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if arr[ni][nj] not in menu_list:
                stack.append((i, j))
                i, j = ni, nj
                visited.append((i, j))
            else:
                return -1
        get_line_sum(i, j, d + 1)
        return
    else:
        while True:
            menu_list.append(arr[i][j])
            ni = i + delta[d][0]
            nj = j + delta[d][1]
            if not 0 <= ni < N or not 0 <= nj < N:
                menu_list.pop()
                if get_line_sum(i, j, d + 1) == -1:
                    i, j = stack.pop()
                else:
                    return len(menu_list)
            if (ni, nj) in visited:
                if stack:
                    menu_list.pop()
                    if get_line_sum(i, j, d + 1) == -1:
                        i, j = stack.pop()
                    else:
                        return len(menu_list)
                else:
                    return -1
            elif arr[ni][nj] not in menu_list:
                stack.append((i, j))
                i, j = ni, nj
                visited.append((i, j))
            else:
                if stack:
                    menu_list.pop()
                    if get_line_sum(i, j, d + 1) == -1:
                        i, j = stack.pop()
                    else:
                        return len(menu_list)
                else:
                    return -1



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mad_max = 0
    for I in range(N):
        for J in range(N):
            if I == 0 or I == N:
                continue
            menu_list = []
            get_line_sum(I, J, 0)

