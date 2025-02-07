import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def find_violet(N):
    board = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        order = list(map(int, input().split()))
        r_point = order[0], order[2]+1
        c_point = order[1], order[3]+1
        color = order[4]
        for i in range(*r_point):
            for j in range(*c_point):
                board[i][j] += color
    purple = 0
    for i in board:
        purple += i.count(3)

    return purple


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {find_violet(N)}')