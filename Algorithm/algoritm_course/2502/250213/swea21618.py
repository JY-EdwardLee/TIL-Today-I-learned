import sys
sys.stdin = open("../../input.txt", "r")


T = int(input())


for tc in range(1, T+1):
    txt = input()
    stack = [0] * len(txt)
    top = -1
    for spell in txt:
        top += 1
        stack[top] = spell
        if top != 0:
            if stack[top-1] == stack[top]:
                top -= 2
    print(f'#{tc} {top+1}')
