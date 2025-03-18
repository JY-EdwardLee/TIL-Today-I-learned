from pydoc import visiblename

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.extend(list(map(int, input().split())))
    arr_p = []
    for i in range(N):
        for j in range(N):
            arr_p.append((i,j))
    cost = 0
    cnt = 0
    goods = list(range(N))
    factory = []
    while cnt < N:
        min_idx = arr.index(min(arr))
        g, f = arr_p.pop(min_idx)
        c = arr.pop(min_idx)
        if f not in factory and g in goods:
            cost += c
            factory.append(f)
            goods.remove(g)
            cnt += 1
    print(f'#{tc} {cost}')