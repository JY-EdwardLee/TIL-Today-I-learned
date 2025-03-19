

def make_set(x):
    parents[x] = x
    return parents


def find_set(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return
    elif ref_x > ref_y:
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parents = [0] * (N+1)
    for i in range(1, N+1):
        make_set(i)
    for i in range(M):
        v = arr[i*2]
        w = arr[i*2 + 1]
        union(v, w)
    groups = set()
    for i in range(1, N+1):
        groups.add(find_set(i))
    print(f'#{tc} {len(groups)}')