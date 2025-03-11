

def get_cross(a, b):
    global crossing
    line.append((a, b))
    M = len(line)
    if M == 1:
        return
    for i, j in line:
        if (i-a)*(j-b) < 0:
            crossing += 1
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    line = []
    crossing = 0
    for _ in range(N):
        A, B = map(int, input().split())
        get_cross(A, B)
    print(f'#{tc} {crossing}')