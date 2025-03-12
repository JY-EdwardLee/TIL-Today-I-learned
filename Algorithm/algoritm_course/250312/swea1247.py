import itertools
import sys
sys.stdin = open("../input.txt", "r")


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def way_back_home(cor):
    s = cor[0], cor[1]
    e = cor[2], cor[3]
    min_dist = float('inf')
    for course in itertools.permutations(range(2, N+2), N):
        client_s  = cor[course[0]*2], cor[course[0]*2 + 1]
        dist = get_dist(s, client_s)
        for i in range(len(course)-1):
            client_s = cor[course[i]*2], cor[course[i]*2 + 1]
            client_e = cor[(course[i+1]) * 2], cor[(course[i+1]) * 2 + 1]
            dist += get_dist(client_s, client_e)
            if dist > min_dist:
                break
        dist += get_dist(client_e, e)
        if min_dist > dist:
            min_dist = dist
    return min_dist

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cor = list(map(int, input().split()))
    print(f'#{tc} {way_back_home(cor)}')