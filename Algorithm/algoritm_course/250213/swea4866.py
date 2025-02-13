import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


for tc in range(1, T+1):
    code = input()
    stack = [0]*len(code)
    top = -1
    ans = 1
    g_dict = {
        ']': '[',
        '}': '{',
        ')': '(',
        }
    for txt in code:
        if txt in '[{(':
            top += 1
            stack[top] = txt
        elif txt in ']})':
            if top == -1:
                ans = 0
            else:
                if g_dict[txt] == stack[top]:
                    top -= 1
                else:
                    ans = 0
    if top != -1:
        ans = 0
    print(f'#{tc} {ans}')