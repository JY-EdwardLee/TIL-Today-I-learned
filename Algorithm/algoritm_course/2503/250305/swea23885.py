T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]*(N+1)
    heap_sum = 0
    for i, num in enumerate(arr):
        c = i+1
        p = c // 2
        heap[c] = num
        # 부모보다 자식이 작다면
        while p != 0 and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p
            p = c//2
    c = N
    while c != 0:
        c = c // 2
        heap_sum += heap[c]
    print(f'#{tc} {heap_sum}')