def f(i, N, s):     # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v

    if i == N:
        if min_v > s:
            min_v = s
    elif min_v < s:     # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
    return min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [i for i in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 10000
    print(f'#{tc} {f(0, N, min_v)}')