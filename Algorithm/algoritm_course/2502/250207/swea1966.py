import sys
sys.stdin = open("input.txt", "r")


T = int(input())


def sorting_function(arr, n):
    counts = [0]*(max(arr)+1)
    temp = [0]*n

    for i in range(n):
        counts[arr[i]] += 1

    for i in range(1, max(arr)+1):
        counts[i] += counts[i-1]

    for i in range(len(arr)-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]

    return temp


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc} {' '.join(map(str,sorting_function(arr, N)))}")

