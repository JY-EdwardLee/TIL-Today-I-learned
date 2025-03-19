import itertools


def valid(M, arr):
    arr.sort(reverse=True)
    max_temp = 0
    for k in range(M, 0, -1):
        for test in itertools.combinations(arr, k):
            temp = 0
            if sum(test) <= C:
                for h in test:
                    temp += h ** 2
                max_temp = max(temp, max_temp)
    else:
        return max_temp

def honey_park(arr, N , M, C):
    global_total = 0
    for i in range(N):
        for j in range(N-(M-1)):
            honey_guy_1 = list(arr[i][j:j+M])
            temp_total = valid(M, honey_guy_1)
            for y in range(i, N):
                if y == i and j + M + M <= N:
                    for l in range(j+M, N-(M-1)):
                        honey_guy_2 = list(arr[y][l:l+M])
                        test_total = temp_total + valid(M, honey_guy_2)
                        if test_total > global_total:
                            global_total = test_total
                elif y == i and j + M + M > N:
                    continue
                else:
                    for l in range(0, N-(M-1)):
                        honey_guy_2 = list(arr[y][l:l+M])
                        test_total = temp_total + valid(M, honey_guy_2)
                        if test_total > global_total:
                            global_total = test_total
    return global_total
T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {honey_park(arr, N, M, C)}')