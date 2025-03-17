

def merge_sort(arr, N):

    m = N//2
    left, right = arr[0:m], arr[m:]

    left = merge_sort(left, len(left))
    right = merge_sort(right, len(right))

    return merge(left, right)


def merge(l, r):
    merged = []
    i, j = 0, 0
    while i + j < l+r:
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    return merged


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))