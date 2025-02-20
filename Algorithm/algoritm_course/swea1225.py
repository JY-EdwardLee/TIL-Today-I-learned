for tc in range(1, 11):
    tc = int(input())
    cque = [0]*9
    front = rear = 0
    for num in list(map(int, input().split())):
        rear = (rear + 1)%9
        cque[rear] = num
    i = 0
    while True:
        i = (i)%5 + 1
        front = (front + 1)%9
        rear = (rear + 1)%9
        cque[rear] = cque[front] - i
        cque[front] = 0
        if cque[rear] <= 0:
            cque[rear] = 0
            break
    # if front < rear:
    #     result = cque[front+1:rear]
    # else:
    #     result = cque[front+1:] + cque[:rear+1]
    result = cque[front+1:rear+1] if front == 0 else cque[front+1:] + cque[:rear+1]
    print(f'#{tc} {" ".join(map(str, result))}')


'''
#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 
'''