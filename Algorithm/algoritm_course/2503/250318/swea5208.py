from collections import deque


def chchchcchange(arr, N):
    i = 0
    cnt = -1
    que = deque()
    while i < N-1:
        battery = arr[i]
        for dist in range(1, 1 + battery):
            que.append((i + dist, cnt+1))
        i, cnt = que.popleft()
    return cnt


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    print(f"#{tc} {chchchcchange(arr, N)}")
