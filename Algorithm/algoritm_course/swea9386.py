import sys
sys.stdin = open("s_input (1).txt", "r")

T = int(input())

def distance(arr, N):
    arr_list = list(str(arr))
    sum_list = [0]
    for i in range(N):
        if arr_list[i] == '0':
            sum_list.append(0)
        else:
            sum_list[-1] += 1
    return max(sum_list)


for tc in range(1, T+1):
    N = int(input())
    arr = input()

    print(f'#{tc} {distance(arr, N)}')