T = int(input())



for tc in range(1, T+1):
    N = int(input())
    time = [0] * 25
    count = 0
    for _ in range(N):
        s, e = map(int,input().split())
        for i in range(s+1, e):
            time[i] += 1
        count += 1

    print(time)

