

def in_order(n):
    if n:
        in_order(left[n])
        word.append(arr[n])
        in_order(right[n])



for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    arr = [0] * (N+1)
    for _ in range(N):
        p, w, l, r = (input().split() + [None] * 4)[:4]
        arr[int(p)] = w
        if l:
            left[int(p)] = int(l)
        if r:
            right[int(p)] = int(r)
    word = []
    in_order(1)
    print(f'#{tc} {"".join(map(str, word))}')