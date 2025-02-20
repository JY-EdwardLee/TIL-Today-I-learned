T = int(input())

# 블록 만들기
# 2X1

# 2x2

# 2x3

# 재귀
def recursion(N, i):
    global count
    # 기저 조건

    if i < N:
        if arr[i] == 0:
            if i == N-1:
                count += 1
                return
            arr[i] = 1
            recursion(N, i+1)
            arr[i] = 0
        if arr[i] == 0:
            if i == N-2:
                count += 1
            arr[i], arr[i+1] = 1, 1
            recursion(N, i + 2)
            arr[i], arr[i + 1] = 0, 0
        if arr[i] == 0:
            if i == N-2:
                count += 1
                return
            arr[i], arr[i+1] = 1, 1
            recursion(N, i + 2)
            arr[i], arr[i + 1] = 0, 0
        if arr[i] == 0:
            if i == N-3:
                count += 1
                return
            arr[i], arr[i+1], arr[i+2] = 1, 1, 1
            recursion(N, i + 2)
            arr[i], arr[i + 1], arr[i+2] = 0, 0, 0

for tc in range(1, T+1):
    N = int(input())
    # 공간
    # 위를 정하면 아래는 정해진다?
    i = 0
    count = 0
    arr = [0] * N # 위 배열
    recursion(N, i)
    print(count)