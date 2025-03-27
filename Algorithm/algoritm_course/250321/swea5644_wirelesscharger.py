# 델타 : 제자리, 상, 우, 하, 좌
delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]


def movings():
    ai, aj, bi, bj = 0, 0, 9, 9
    count_A[0] = arr[0][0]
    count_B[0] = arr[9][9]
    for L in range(M):
        ai, aj = ai + delta[arr_A[L]][0], aj + delta[arr_A[L]][1]
        bi, bj = bi + delta[arr_B[L]][0], bj + delta[arr_B[L]][1]
        count_A[L+1] = arr[ai][aj]
        count_B[L+1] = arr[bi][bj]



T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split())
    arr_A = list(map(int, input().split()))
    arr_B = list(map(int, input().split()))
    arr = [list([] for _ in range(10)) for _ in range(10)]
    count_A, count_B = [0]*(M+1), [0]*(M+1)
    charger = {}
    for L in range(A):
        x, y, c, p = map(int, input().split())
        charger[L] = p
        x -= 1
        y -= 1
        for i in range(10):
            for j in range(10):
                if abs(i - y) + abs(j - x) <= c:
                    arr[i][j].append(L)
    movings()
    total = 0
    for m, n in zip(count_A, count_B):
        max_round = 0
        if m and n :
            for l in m:
                for r in n:
                    if l == r:
                        max_round = max(max_round, (charger[l]))
                    else:
                        max_round = max(max_round, (charger[l] + charger[r]))
        elif m:
            for l in m:
                max_round = max(max_round, charger[l])
        elif n:
            for l in n:
                max_round = max(max_round, charger[l])
        total += max_round
    print(f'#{tc} {total}')

