import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def paris_dist(d, a, b, f):
    flag = 1
    dist = 0
    while round(d, 100) > 0:
        if flag:
            # 거리 = 속력/시간
            # 시간 = (기차속력 + 파리속력)/거리
            x = (b + f)/d
            # 한 번 부딪혔을 때 줄어든 거리 = 거리 - b속력/시간 - a속력/시간
            d = d - b/x - a/x
            dist += f/x
            flag = 0
        else:
            x = (a + f)/d
            d = d - b/x - a/x
            dist += f/x
            flag = 1
    return dist

for tc in range(1, T+1):
    d, a, b, f = map(int, input().split())
    print(paris_dist(d, a, b, f))

