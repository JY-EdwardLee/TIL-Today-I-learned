T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    front = -1
    rear = N - 1
    queue = (list(map(int, input().split())))
    queue.append(0)
    for _ in range(M):
        # deQueue
        front = (front+1)%(N+1)
        x = queue[front]
        queue[front] = 0
        # enQueue
        rear = (rear+1)%(N+1)
        queue[rear] = x
    else:
        start = queue.index(0)
    print(f'#{tc} {queue[(front+1)%(N+1)]}')