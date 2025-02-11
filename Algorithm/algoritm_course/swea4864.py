import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def compare_str(str_1, str_2):
    N = len(str_2) - len(str_1)
    for i in range(N):
        if str_1 == str_2[i:i+len(str_1)]:
            return 1
    else:
        return 0

for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    print(f'#{tc} {compare_str(str_1, str_2)}')
