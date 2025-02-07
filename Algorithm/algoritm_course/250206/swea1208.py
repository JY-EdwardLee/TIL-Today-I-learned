import sys
sys.stdin = open("s_input (1).txt", "r")

T = 10

def dump(arr, N):
    for _ in range(N):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
        # if max(arr) - min(arr) <= 1:
        #     break
    return max(arr) - min(arr)

for tc in range(1, T+1):
    N = int(input())        # 덤프횟수 N
    arr = list(map(int, input().split()))
    print(f'#{tc} {dump(arr, N)}')