# import sys
# sys.stdin = open('input.txt', "r")


T = int(input())


def count_dot(n):
    count = 0
    for i in range(-n, n+1):
        for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                count += 1
    return count


for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {count_dot(N)}')
