T = int(input())
for tc in range(1, T+1):
    x_1, x_2, y_1, y_2 = map(int, input().split())
    result = 0
    if x_1 <= y_1:
        if y_1 >= x_2:
            pass
        else:
            if x_2 >= y_2:
                result = y_2 - y_1
            else:
                result = x_2 - y_1
    else:
        if x_1 >= y_2:
            pass
        else:
            if y_2 >= x_2:
                result = x_2 - x_1
            else:
                result = y_2 - x_1
    print(f'#{tc} {result}')