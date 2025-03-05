

def cal(m):
    if m not in '+-*/':
        stack.append(m)
    else:
        n1 = int(stack.pop())
        n2 = int(stack.pop())
        if m == '+':
            stack.append(n2 + n1)
        if m == '-':
            stack.append(n2 - n1)
        if m == '*':
            stack.append(n2 * n1)
        if m == '/':
            stack.append(n2 // n1)

def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        cal(arr[n])

for tc in range(1, 11):
    N = int(input())
    arr = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for _ in range(N):
        p, n, l, r = (input().split() + [None] * 2)[:4]
        arr[int(p)] = n
        if l:
            left[int(p)] = int(l)
            right[int(p)] = int(r)
    stack = []
    postorder(1)
    print(f'#{tc} {stack[0]}')


'''
#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2
'''