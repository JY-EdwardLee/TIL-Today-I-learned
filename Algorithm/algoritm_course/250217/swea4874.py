import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def cal(post_fix):
    stack = []
    for x in post_fix:
        if x not in '/*-+.':
            stack.append(int(x))
        elif x == '.':
            if len(stack) == 1:
                result = stack.pop()
                break
            else:
                return 'error'
        else:
            if not stack:
                return 'error'
            o2 = stack.pop()
            if not stack:
                return 'error'
            o1 = stack.pop()
            if x == '/':
                data = o1 // o2
                stack.append(data)
            elif x == '*':
                data = o1 * o2
                stack.append(data)
            elif x == '-':
                data = o1 - o2
                stack.append(data)
            elif x == '+':
                data = o1 + o2
                stack.append(data)
    return result


for tc in range(1, T+1):
    post_fix = input().split()
    result = cal(post_fix)
    print(f'#{tc} {result}')