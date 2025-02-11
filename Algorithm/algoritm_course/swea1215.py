import sys
sys.stdin = open("input.txt", "r")


def search_wyw(arr, n):
    # loop
    count = 0
    for i in range(8):
        for j in range(8 + 1 - n):
            # 가로 회문 탐색
            garo_word = arr[i][j:j+n]
            if garo_word == garo_word[::-1]:
                count += 1

    # 세로 회문 탐색
    for i in range(8):
        for j in range(8 - n + 1):
            sero_word = ''
            for s in range(j, j+n):
                sero_word += arr[s][i]
            if sero_word == sero_word[::-1]:
                count += 1

    return count

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    print(f'#{tc} {search_wyw(arr, N)}')