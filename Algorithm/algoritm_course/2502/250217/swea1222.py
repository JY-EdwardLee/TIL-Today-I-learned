import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    in_fix = input().strip()
    stack = []
    post_fix = ''
    for x in in_fix:
        if x != '+':
            post_fix += x
        else:
            if not stack:
                stack.append(x)
            elif stack:
                post_fix += x
    else:
        post_fix += stack.pop()
    for x in post_fix:
        if x != '+':
            stack.append(x)
        else:
            o1 = int(stack.pop())
            o2 = int(stack.pop())
            stack.append(o1 + o2)
    else:
        result = stack.pop()
    print(f'#{tc} {result}')
