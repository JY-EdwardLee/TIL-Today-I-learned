import sys
sys.stdin = open("input.txt", "r")


def line(guide, n):
    stack = []
    cnt = 0
    for i in range(n):
        if guide[i] == '(':
        elif guide[i] == ')':
            if stack:
               if stack[-1] == '(':
                   stack.pop()

            else:
                break


def cutting(guide, n):
    lines = line(guide, n)



T = int(input())
for tc in range(1, T+1):
    guide = input().strip()
    N = len(guide)
