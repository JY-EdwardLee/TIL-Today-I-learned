def cal(x, y, c):
    if c == 0:
        return x + y
    elif c == 1:
        return x - y
    elif c == 2:
        return x*y
    elif c == 3:
        return x//y

def dfs(i):
    if i == N:
        max_sum, min_sum = max(max_sum, ), min(min_sum, )
        return

    dfs(i+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tool = list(input().split())
    nums = list(map(int, input().split()))
    tooltool = []
    for i in tool:
        tooltool.append()
    max_sum = 0
    min_sum = float('inf')
    dfs(0, )