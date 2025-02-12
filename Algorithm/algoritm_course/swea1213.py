import sys
sys.stdin = open('input.txt', encoding='utf-8')


def count_word(search_w, search_s):
    N = len(search_w)
    M = len(search_s)
    i = j = N-1
    cnt = 0
    while i < M:
        x = search_s[i]
        if search_s[i] == search_w[-1]:
            if search_s[i-(N-1):i+1] == search_w:
                cnt += 1
            i += N
        elif search_s[i] in search_w:
            j = search_w.index(search_s[i])
            word = search_s[i-j:i+N-j]
            if word == search_w:
                cnt += 1
                i += N
            else:
                i = i + N - j
        else:
            i += N

    return cnt



for tc in range(1, 11):
    tc = int(input())
    N = input().strip()
    M = input().strip()
    print(f'#{tc} {count_word(N, M)}')