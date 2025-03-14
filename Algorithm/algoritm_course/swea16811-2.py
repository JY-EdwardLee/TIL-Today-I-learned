import itertools


def check_valid(comb):
    a, b, c = comb
    s, j, d = arr[:a], arr[a:a + b], arr[a + b:]
    # 경계에서 크기가 같은지 체크(안전한 방법)
    if s[-1] == j[0] or j[-1] == d[0]:
        return False
    return True


def get_minimum(comb):
    if not check_valid(comb):
        return False
    return max(comb) - min(comb)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = sorted(map(int, input().split()))
    min_pack = N  # 최대차이는 N개 이하임
    podium = set(itertools.product(range(1, N // 2 + 1), repeat=3))
    for a, b, c in podium:
        print(a, b, c)
        if a + b + c == N:
            comb = (a, b, c)
            ans = get_minimum(comb)
            if ans is not False:
                min_pack = min(ans, min_pack)

    if min_pack == N:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_pack}')
