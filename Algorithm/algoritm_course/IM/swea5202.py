T = int(input())



for tc in range(1, T+1):
    N = int(input())
    time = [0] * 25
    s_list = []
    e_list = []
    count = 0
    for _ in range(N):
        s, e = map(int,input().split())
        s_list.append(s)
        e_list.append(e)
    time_spend = [s-e for s, e in zip(e_list, s_list)]
    t = 0
    while t < N:
        min_index  = time_spend.index(min(time_spend))
        if 1 not in time[s_list[min_index]:e_list[min_index]]:
            count += 1
            for i in range(s_list[min_index], e_list[min_index]):
                time[i] += 1
        time_spend.pop(min_index)
        s_list.pop(min_index)
        e_list.pop(min_index)
        t += 1

    print(f'#{tc} {count}')

