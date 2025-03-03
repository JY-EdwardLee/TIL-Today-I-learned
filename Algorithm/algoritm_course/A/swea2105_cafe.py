from collections import deque
# 델타 정방향
delta = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def get_sum():



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    mad_max = 0
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N:
                continue


