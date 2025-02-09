# import sys
# sys.stdin = open('input.txt', 'r')

'''
3
3 6
5 15
5 10

'''

T = int(input())


def search_subset(n, k):
    arr = range(1, 13)
    result = 0
    for i in range(1<<12):
        subset_list = []
        for j in range(0, 12):
            if i & (1<<j):
                subset_list.append(arr[j])
        if sum(subset_list) == k and len(subset_list) == n:
            result += 1
    return result


for tc in range(1, T+1):
    # 원소 개수 N, 원소의 합 K
    N, K = map(int, input().split())

    print(f'#{tc} {search_subset(N, K)}')
