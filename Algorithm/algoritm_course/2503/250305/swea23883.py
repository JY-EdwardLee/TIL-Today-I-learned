

def in_order(p):
    c = p * 2
    if p < N:
        in_order(c)
        arr[p] = que.pop(0)
        in_order(c + 1)
    elif p == N:
        in_order(c)
        arr[p] = que.pop(0)




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    que = list(range(1, N+1))
    in_order(1)
    print(f'#{tc} {arr[1]} {arr[N // 2]}')