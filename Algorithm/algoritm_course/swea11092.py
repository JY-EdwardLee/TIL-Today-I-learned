'''
3
5
1 1 2 3 3
10
3 10 5 5 8 3 9 1 3 3
20
4 1 6 7 9 4 1 4 8 4 1 6 5 3 1 4 3 1 10 10

'''
T = int(input())

def distance(arr, N):
    min_index = 0
    max_index = 0
    for i in range(0, N):
        if arr[i] < arr[min_index]:
            min_index = i
        if arr[i] >= arr[max_index]:
            max_index = i
    return abs(max_index-min_index)

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {distance(arr, N)}')