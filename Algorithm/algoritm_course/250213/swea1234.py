import sys
sys.stdin = open("../input.txt", "r")

for tc in range(1, 11):
    N, memo = map(str, input().split())
    stack = [0] * int(N)     # N개의 스택 생성
    top = -1    # top은 -1
    for num in memo:
        if top == -1:
            # 시작점은 항상 stack.append(num)
            top += 1
            stack[top] = num
        else:
            # 숫자가 연속하는 지 검증
            if stack[top] == num:
                # 연속하면 stack.pop()
                top -= 1
            else:
                # 연속하지 않은 다면 stack.append(num)
                top += 1
                stack[top] = num
    # 만들어 놓은 배열에서 0 제거 (top은 만들어진 인덱스와 같은 곳을 바라보기에 top(표기상 top+1)까지 슬라이싱)
    password = stack[:top+1]
    print(f'#{tc} {"".join(map(str, password))}')