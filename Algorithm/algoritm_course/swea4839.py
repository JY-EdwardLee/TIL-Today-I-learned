import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


def bin_search(page, pa, pb):
    a_start = 1
    a_end = page
    a_count = 0
    while a_start <= a_end:
        a_middle = (a_start + a_end) // 2
        if pa == a_middle:
            break
        else:
            a_count += 1
            if pa < a_middle:
                a_end = a_middle
            else:
                a_start = a_middle

    b_start = 1
    b_end = page
    b_count = 0
    while b_start <= b_end:
        b_middle = (b_start + b_end) // 2
        if pb == b_middle:
            break
        else:
            b_count += 1
            if pb < b_middle:
                b_end = b_middle
            else:
                b_start = b_middle

    if a_count > b_count:
        return "B"
    elif b_count > a_count:
        return "A"
    else:
        return 0


for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    print(f"#{tc} {bin_search(P, A, B)}")