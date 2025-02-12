import sys
sys.stdin = open("input.txt", "r")


T = int(input())


def switch_box(n, q):
    boxes = [0]*n # 0이라 적힌 N가지 박스
    for _ in range(q):
        L, R = map(int, input().split())
        for i in range(L-1, R-1):
            boxes[i] += 1
    return boxes



for tc in range(1, T+1):
    N, Q = map(int, input().split())
    print(f'#{tc} {' '.join(map(str,switch_box(N,Q)))}')