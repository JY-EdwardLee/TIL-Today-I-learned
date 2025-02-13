T = int(input())


def pascal(n):
    stack = [0] * n     # 스택 생성
    top = -1    # top 세팅
    # 기저 조건
    if n == 1:
        top += 1
        stack[top] = 1
        return stack
    # 유도 부분
    for _ in range(n):
        if (top == -1) or (top == n - 2):
            top += 1
            stack[top] = 1
        else:
            top += 1
            stack[top] = pascal(n-1)[top-1] + pascal(n-1)[top]
    return stack


for tc in range(1, T+1):
    N = int(input())
    triangle = []
    print(f'#{tc}')
    for floor in range(1, N+1):
        print(*pascal(floor))
