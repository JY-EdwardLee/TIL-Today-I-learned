from collections import deque
# 델타 : 상(초기 방향), 우, 하, 좌
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 델타 +1 우측바향, 델타 -1 좌측 방향

# 방향 돌리기
def turn():

# 전진하기
def go(i, j, k):
    ni = i + di
    nj = j + dj
    if 0 <= ni < N and 0 <= nj < N:
        # 나무 베기
        if arr[ni][nj] == 'T' and k > 0:
            k -= 1
            return ni, nj, k
        elif arr[ni][nj] != 'T':
            return ni, nj, k
        else:
            return -1


def bfs(arr, n, k):
    que = deque()



T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

        # 전진하기 + 나무 베기
