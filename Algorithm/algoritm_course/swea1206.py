'''
10
0 0 254 185 76 227 84 175 0 0
10
0 0 251 199 176 27 184 75 0 0
11
0 0 118 90 243 178 99 100 200 0 0

'''
T = 10

def num_of_view(arr, N):
    view = 0
    for i in range(2, N-1):
        if arr[i] >= max(arr[i-2:i+3]):
            view += arr[i] - max(max(arr[i-2:i]), max(arr[i+1:i+3]))
    return view

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc} {num_of_view(arr, N)}')