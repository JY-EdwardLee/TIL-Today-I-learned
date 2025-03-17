import sys
sys.stdin = open('../../input.txt', 'r')


def euiseoki(case_list):
    # max_len = 0
    euiseoksik_word = ""
    # for i in case_list:
    #     max_len = max(max_len, len(i))
    max_len = max(map(len,case_list))
    for i in range(max_len):
        for j in range(len(case_list)):
            try:
                euiseoksik_word += case_list[j][i]
            except IndexError:
                continue
    return euiseoksik_word


T = int(input())

for tc in range(1, T+1):
    case_list = [input() for _ in range(5)]
    print(f'#{tc} {euiseoki(case_list)}')