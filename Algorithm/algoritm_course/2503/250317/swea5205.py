

def quickSort(arr, N):
    if N == 1 or N == 0:
        return arr
    piv = arr[0]
    left, right = [], []
    for i in range(1, N):
        if arr[i] < arr[0]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = quickSort(left, len(left))
    right = quickSort(right, len(right))

    return left + [piv] + right

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = quickSort(arr, N)
    print(f'#{tc} {sorted_arr[N//2]}')