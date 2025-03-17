import sys
sys.stdin = open("../../input.txt", "r")


T = int(input())


def rolling_pasta(arr):
    # 90도 회전하기
    arr_90 = [_ for _ in map(list, zip(*arr[::-1]))]
    # 180도 회전하기
    arr_180 = [_ for _ in map(list, zip(*arr_90[::-1]))]
    # 270도 회전하기
    arr_270 = [_ for _ in map(list, zip(*arr))][::-1]
    return arr_90, arr_180, arr_270

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90, arr_180, arr_270 = rolling_pasta(arr)
    a = ["".join(map(str, arr_90[i])) for i in range(N)]
    b = ["".join(map(str, arr_180[i])) for i in range(N)]
    c = ["".join(map(str, arr_270[i])) for i in range(N)]
    print(f'#{tc}')
    for x in zip(a, b, c):
        print(" ".join(x))