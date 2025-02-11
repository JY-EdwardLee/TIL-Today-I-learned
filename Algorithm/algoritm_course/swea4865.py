import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def count_str(str_1, str_2):
    N = len(str_1)
    M = len(str_2)
    max_text_count = 0
    for i in range(N):
        text_count = 0
        for j in range(M):
            if str_1[i] == str_2[j]:
                text_count += 1
        max_text_count = max(max_text_count, text_count)
    return max_text_count


for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    print(f'#{tc} {count_str(str_1, str_2)}')