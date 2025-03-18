

def find_rel(a, group):
    for i in following[a]:
        if i not in group:
            group.append(i)
            find_rel(i, group)
    return group


def count_group(arr, N, M):
    cnt = 0
    while arr:
        fm = arr[0]
        group = [arr[0]]
        grouped = find_rel(fm, group)
        arr = [x for x in arr if x not in grouped]
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    following = [[] for _ in range(N+1)]
    for _ in range(M):
        v, w = map(int, input().split())
        following[v].append(w)
        following[w].append(v)
        # ??? 왜지

    print(f'#{tc} {count_group(list(range(1, N+1)), N, M)}')