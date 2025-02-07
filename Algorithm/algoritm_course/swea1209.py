import sys
sys.stdin = open("input.txt", "r")

T = 10

def find_max(arr):
    # 행 합
    raw_max = 0
    for i in range(100):
        if raw_max < sum(arr[i]):
            raw_max = sum(arr[i])
    # 열 합
    col_max = 0
    for j in range(100):
        j_max = 0
        for i in range(100):
            j_max += arr[i][j]
        if col_max < j_max:
            col_max = j_max
    # 45도 합
    sum_45 = 0
    for i, j in zip(range(100), range(100)):
        sum_45 += arr[i][j]
    # 135도 합
    sum_135 = 0
    for i, j in zip(range(100), range(99, 0, -1)):
        sum_135 += arr[i][j]
    return max(raw_max, col_max, sum_135, sum_45)

for tc in range(1, T+1):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{tc} {find_max(arr)}')