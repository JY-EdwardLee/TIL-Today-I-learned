icp = {'+': 1,
       '*': 2,
       }

for tc in range(1, 11):
    N = int(input())
    infix = input().strip()
    postfix = ''
    stack = []
    for j in range(N):
        if infix[j] not in '*+':
            postfix += infix[j]
        else:
            while stack and icp[infix[j]] <= icp[stack[-1]]:
                postfix += stack.pop()
            stack.append(infix[j])
    while stack:
        postfix += stack.pop()

    for i in range(N):
        if postfix[i] not in '*+':
            stack.append(int(postfix[i]))
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            if postfix[i] == '*':
                stack.append(o2*o1)
            if postfix[i] == '+':
                stack.append(o2+o1)
    else:
        result = stack.pop()
    print(f'#{tc} {result}')

