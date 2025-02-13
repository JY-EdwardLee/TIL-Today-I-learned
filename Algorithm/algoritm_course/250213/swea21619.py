import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def my_push(n):
    global t
    t += 1
    stack[t] = n

def my_pop(n):
    global t
    t -= 1


for tc in range(1, T+1):
    N = input()
    stack = [0] * len(N)
    ans = 1
    t = -1
    for i in N:
        if i == '(':
            my_push(i)
        elif i == ')':
            if t == -1:
                ans = -1
            else:
                my_pop(i)
    if t != -1:
        ans = -1
    print(f'#{tc} {ans}')