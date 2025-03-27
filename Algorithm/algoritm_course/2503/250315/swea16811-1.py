

def pack_carrot(arr, N):
    min_diff = float('inf')
    for i in range(1, N//2+1):  # 소 찾기
        for j in range(1, N//2+1):  # 중 찾기
            S, J, D = arr[:i], arr[i:i+j], arr[i+j: N]
            # [1][2][3,4,5,6,7,8] => [1][2,3][4,5,6,7,8]=> [1][2,3,4][5,~~]
            # => [1,2][3][4,5,6,7,8] => [1,2,3][4][5,6,7,8]
            # [1,2,3,4][5,6,7,8][]
            # [1,1][1,2][2,3]
            if len(S) > N//2 or len(D) > N//2 or len(D) > N//2:     # 한 상자가 절반 넘게 담지마라
                continue
            if len(S) == 0 or len(D) == 0 or len(J) == 0:           # 빈 상자가 있으면 지나쳐라
                continue
            if S[-1] == J[0] or J[-1] == D[0]:                      # 같은 무게가 다른 상자에 들어있으면 지나쳐라
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