import sys
sys.stdin = open("../input.txt", "r")


T = int(input())

def check_runway(road, n, x):
    slides = [0] * n
    for i in range(n-1):
        # 두 칸 뛰기는 안되니 차이가 2 이상이면 리턴 0
        if 1 < abs(road[i] - road[i+1]):
            return 0
        # 한 칸 올라갈 시
        elif road[i] + 1 == road[i+1]:
            # 낭떠러지거나 경사로가 있는지 점검
            if (i - x + 1 < 0) or (-1 in slides[i-x+1:i+1]):
                return 0
            # 경사로를 세울 수 있으면 세우고 그 자리에 -1 표시
            if len(set(road[i-x+1:i])) == 1:
                for a in range(i-x+1, i+1):
                    slides[a] = -1
            else:
                return 0
        # 한 칸 내려갈 시
        elif road[i] - 1 == road[i+1]:
            # 낭떠러지가 있는 지 점검
            if i + x >= n:
                return 0
            # 경사로를 세울 수 있으면 세우고 그 자리에 -1 표시
            if len(set(road[i+1:i+1+x])) == 1:
                for a in range(i+1, i+1+x):
                    slides[a] = -1
            else:
                return 0
    else:
        return 1

for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    avail_road = 0
    for row in arr:
        avail_road += check_runway(row, N ,X)

    arr = [list(line) for line in zip(*arr)]
    for col in arr:
        avail_road += check_runway(col, N, X)

    print(f'#{tc} {avail_road}')
