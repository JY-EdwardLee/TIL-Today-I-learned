import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def runway(arr, n, x):
    availabe_runway = 0
    # 가로 활주로 점검
    for row in range(n):
        # 하나의 숫자로만 이루어져 있으면 활주로 아묻따 O
        if len(set(arr[row])) == 1:
            availabe_runway += 1
            continue    # for i in range(n)
        # 두개 이상의 숫자로 이루어져 있으면 활주로 가능성 점검
        slides = [0] * n     # 경사로 세웠는지 확인용 리스트
        for col in range(n-1):
            # 높아지면 x만큼 뒤를 본다
            if arr[row][col] + 1 == arr[row][col+1]:
                # 낭떠러지가 아니고 세워둔 경사로가 없으면
                if (col + 1 - x >= 0) and (-1 not in slides[col-x:col]):
                    # 경사로를 둘 수 있으면
                    if len(set(arr[row][col-x+1:col+1])) == 1:
                        # 경사로를 둔다 (-1)
                        for slide in range(col-x+1, col+1):
                            slides[slide] = -1
                # 낭떠러지거나 세워둔 경사로가 있으면
                else:
                    # loop를 탈출한다
                    break   # for col

            # 낮아지면 x만큼 앞을 본다
            elif arr[row][col] - 1 == arr[row][col+1]:
                # 낭떠러지가 아니면
                if col + x < n:
                    # 경사로를 둘 수 있으면
                    if len(set(arr[row][col+1:col+x+1])) == 1:
                        # 차분하게 내려간다
                        continue    # for col in range(n)
                    # 경사로를 둘 수 없으면
                    else:
                        # loop를 탈출 한다
                        break       # for col in range(n)
                # 낭떠러지면
                else:
                    # loop를 탈출한다
                    break   # for col in range(n)
            elif arr[row][col] == arr[row][col+1]:
                continue
            else:
                break
        else:
            availabe_runway += 1
    # 세로 활주로 점검
    arr = [list(line) for line in zip(*arr)]
    for row in range(n):
        # 하나의 숫자로만 이루어져 있으면 활주로 아묻따 O
        if len(set(arr[row])) == 1:
            availabe_runway += 1
            continue    # for i in range(n)
        # 두개 이상의 숫자로 이루어져 있으면 활주로 가능성 점검
        slides = [0] * n     # 경사로 세웠는지 확인용 리스트
        for col in range(n-1):
            # 높아지면 x만큼 뒤를 본다
            if arr[row][col] + 1 == arr[row][col+1]:
                # 낭떠러지가 아니고 세워둔 경사로가 없으면
                if (col + 1 - x >= 0) and (-1 not in slides[col+1-x:col]):
                    # 경사로를 둘 수 있으면
                    if len(set(arr[row][col-x+1:col+1])) == 1:
                        # 경사로를 둔다 (-1)
                        for slide in range(col-x+1, col+1):
                            slides[slide] = -1
                # 낭떠러지거나 세워둔 경사로가 있으면
                else:
                    # loop를 탈출한다
                    break   # for col

            # 낮아지면 x만큼 앞을 본다
            elif arr[row][col] - 1 == arr[row][col+1]:
                # 낭떠러지가 아니면
                if col + x < n:
                    # 경사로를 둘 수 있으면
                    if len(set(arr[row][col+1:col+x+1])) == 1:
                        # 경사로를 둔다 (-1)
                        for slide in range(col+1, col+1+x):
                            slides[slide] = -1
                        # 차분하게 내려간다
                        continue    # for col in range(n)
                    # 경사로를 둘 수 없으면
                    else:
                        # loop를 탈출 한다
                        break       # for col in range(n)
                # 낭떠러지면
                else:
                    # loop를 탈출한다
                    break   # for col in range(n)
            elif arr[row][col] == arr[row][col+1]:
                continue
            else:
                break
        else:
            availabe_runway += 1

    return availabe_runway


for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {runway(arr, N, X)}')
