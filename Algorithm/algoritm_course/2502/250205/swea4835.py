'''
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176

'''
T = int(input())

def part_sum(arr, N, M):
    min_sum = sum(arr[0:M])
    max_sum = sum(arr[0:M])

    for i in range(1, N+1-M):
        if sum(arr[i:i+M]) > max_sum:
            max_sum = sum(arr[i:i+M])
        if sum(arr[i:i+M]) < min_sum:
            min_sum = sum(arr[i:i+M])
    return max_sum - min_sum

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{tc} {part_sum(arr, N, M)}')