

def get_sub(N):
    global cnt
    if N:
        cnt += 1
        get_sub(left[N])
        get_sub(right[N])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (ma x(arr) + 1)
    right = [0] * (max(arr) + 1)
    for i in range(max(arr)-1):
        v, e = arr[i*2], arr[i*2 + 1]
        if left[v] == 0:
            left[v] = e
        else:
            right[v] = e
    cnt = 0
    get_sub(N)
    print(f'#{tc} {cnt}')