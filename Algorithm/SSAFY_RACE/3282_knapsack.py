T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    goods = [[0,0]]
    for _ in range(N):
        goods.append(list(map(int, input().split())))
    knap_sack = list([0]*(K+1) for _ in range(N+1))
    for n in range(N+1):
        knap_sack[n][0] = 0
    for k in range(K):
        knap_sack[0][k] = 0
    for n in range(1, N+1):
        for k in range(1, K+1):
            if k - goods[n][0] >= 0:
                knap_sack[n][k] = max(knap_sack[n-1][k], knap_sack[n-1][k -goods[n][0]] + goods[n][1])
            else:
                knap_sack[n][k] = knap_sack[n-1][k]
    print(f'#{tc} {knap_sack[n][k]}')