import sys
sys.stdin = open("../input.txt", "r")

T = int(input())


def selecting_sort(arr, n):
    for i in range(n):
        if i%2 == 0:
            max_index = i
            for j in range(i+1, n):
                if arr[max_index] < arr[j]:
                    arr[j], arr[max_index] = arr[max_index], arr[j]
        if i%2 == 1:
            min_index = i
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    arr[j], arr[min_index] = arr[min_index], arr[j]
    return arr[:10]



for tc in range(1, T+1):
    # 배열의 길이 N 받음
    N = int(input())
    # 배열 arr 받음
    arr = list(map(int, input().split()))
    print(f'#{tc} {" ".join(map(str, selecting_sort(arr, N)))}')
