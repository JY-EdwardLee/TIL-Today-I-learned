from collections import deque


def merge_sort(arr, N):
    if len(arr) == 1:
        return arr
    m = N//2
    left, right = arr[:m], arr[m:]

    left = merge_sort(left, len(left))
    right = merge_sort(right, len(right))

    return merge(left, right)


def merge(l, r):
    global total
    merged = []
    if l[-1] > r[-1]:
        total += 1
    i, j = 0, 0
    N, M = len(l), len(r)
    while i < N and j < M:
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    if i < N:
        merged.extend(l[i:])
    if j < M:
        merged.extend(r[j:])
    return merged


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0

    print(f'#{tc} {merge_sort(arr, N)[N//2]} {total}')