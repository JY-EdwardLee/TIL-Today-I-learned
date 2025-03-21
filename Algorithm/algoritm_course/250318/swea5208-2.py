def check(start, cnt):
    global result
    if cnt > result:
        return

    if start >= N - 1:
        result = min(result, cnt)
        return
    for i in range(1, bus_stop[start] + 1):
        if start + i < N:
            check(start + i, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    ipt = list(map(int, input().split()))
    N = ipt[0]
    bus_stop = ipt[1:]
    result = 10000
    check(0, 0)
    print(f'#{tc} {result - 1}')