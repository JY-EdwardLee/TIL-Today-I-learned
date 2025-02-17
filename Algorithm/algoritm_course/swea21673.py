import sys
sys.stdin = open("input.txt", "r")


icp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}
T = int(input())

for tc in range(1, T+1):
    in_fix = input().strip()
    stack = []
    post_fix = ''
    for x in in_fix:
        if x not in '()*/+-':
            post_fix += x
        elif x == ')':
            while stack[-1] != '(':
                post_fix += stack.pop()
        else:
            if not stack or isp[stack[-1]] < icp[x]:
                stack.append(x)
            elif isp[stack[-1]] >= icp[x]:
                while len(stack) != 0 and isp[stack[-1]] >= icp[x]:
                    post_fix += stack.pop()
                stack.append(x)
    else:
        while stack:
            post_fix += stack.pop()

    print(f'#{tc} {post_fix}')
