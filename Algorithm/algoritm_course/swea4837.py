T = int(input())


def search_subset(n, k):



for tc in range(1, T+1):
    N, K = map(int, input().split())

    print(f'#{tc} {search_subset(N, K)}')
