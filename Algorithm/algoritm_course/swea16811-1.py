

def pack_carrot(arr, N):
    min_diff = float('inf')
    for i in range(1, N//2+1):
        for j in range(1, N//2+1):
            S, J, D = arr[:i], arr[i:i+j], arr[i+j: N]
            if len(S) > N//2 or len(D) > N//2 or len(D) > N//2:
                continue
            if len(S) == 0 or len(D) == 0 or len(J) == 0:
                continue
            if S[-1] == J[0] or J[-1] == D[0]:
                continue
            diff = max(abs(len(S) - len(J)), abs(len(J) - len(D)), abs(len(D) - len(S)))
            min_diff = min(diff, min_diff)
    if min_diff == float('inf'):
        return -1
    else:
        return min_diff



T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f'#{tc} {pack_carrot(arr, N)}')