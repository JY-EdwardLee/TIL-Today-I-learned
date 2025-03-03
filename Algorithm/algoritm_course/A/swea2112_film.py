
T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    for i in range(D):
        if i == 0:
            arr_num = [[1] * W]
        else:
            next_num = list(map(lambda x, y: x == y, arr[i], arr[i - 1]))
            arr_num.append(list(map(lambda x, y: x + y if y else 1, arr_num[i-1], next_num)))
