import sys
import itertools
sys.stdin = open("../input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    subset = list(itertools.permutations(range(2,N+1), N-1))
    total_cost = float('inf')
    for order in subset:
        cost = arr[0][order[0]-1]
        i = 0
        while i < N-2:
            y, x = order[i]-1, order[i+1]-1
            cost += arr[y][x]
            i += 1
        cost += arr[order[-1]-1][0]
        total_cost = min(total_cost, cost)
    print(f'#{tc} {total_cost}')