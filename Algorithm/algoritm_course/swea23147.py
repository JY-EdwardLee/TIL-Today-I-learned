'''
7
9
7 4 2 0 0 6 0 7 0
9
100 99 95 99 100 0 1 2 5
7
3 2 3 4 5 6 7
1
0
1
1
4
0 0 0 0
5
2 2 2 2 2

'''

T = int(input())

def max_drop(arr, N):
    max_drop = 0
    for i in range(0, N):
        drop = 0
        for j in range(i+1, N):
            if arr[j] < arr[i]:
                drop += 1
        if max_drop < drop:
            max_drop = drop
    return max_drop

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {max_drop(arr,N)}')