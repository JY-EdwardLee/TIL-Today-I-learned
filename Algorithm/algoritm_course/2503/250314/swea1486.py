

def chyomondo(arr, height):
    global min_diff
    M = len(arr)
    for i in range(M):
        if height - arr[i] >= B:
            min_diff = min(min_diff, (height - arr[i]) - B)
            chyomondo(arr[i+1:], height - arr[i])
        # elif height - arr[i] == B:
        #     min_dff = 0
        #     return
        else:
            continue


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    max_height = sum(arr)
    min_diff = max_height - B
    chyomondo(arr, max_height)
    print(f'#{tc} {min_diff}')