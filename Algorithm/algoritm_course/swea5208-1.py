from collections import deque


def chchchcchange(arr, N):
    i = 0
    cnt = 0
    max_dist = 0
    if arr[0] + 1 == N:
        return cnt
    while max_dist < N-1:
        max_far = i
        battery = arr[i]
        for j in range(1, 1 + battery):
            if max_dist <= arr[j+i] + i + j:
                max_dist = arr[j+i] + i + j
                max_far = j + i
            if max_dist >= N-1:
                cnt += 1
                return cnt
        i = max_far
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    print(f"#{tc} {chchchcchange(arr, N)}")
'''
2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''