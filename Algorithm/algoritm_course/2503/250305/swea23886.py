

def find_nod(p):
    try:
        if arr[p] != 0:
           return arr[p]
        elif arr[p] == 0:
            c1 = p*2
            c2 = p*2 + 1
            arr[p] = find_nod(c1) + find_nod(c2)
            return arr[p]
    except IndexError:
        return 0

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)

    for _ in range(M):
        nod, v = map(int, input().split())
        arr[nod] = v
    find_nod(1)
    print(f'#{tc} {arr[L]}')