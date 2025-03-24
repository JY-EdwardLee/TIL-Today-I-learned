T = int(input())

for tc in range(1, T+1):
    sx, ex, sy, ey = map(int, input().split())
    time = [0] * 101
    for i in range(sx, ex):
        time[i] += 1
    for j in range(sy, ey):
        time[j] += 1
    print(f'#{tc} {time.count(2)}')