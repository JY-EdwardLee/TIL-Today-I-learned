import sys
sys.stdin = open('input.txt', 'r')


T = int(input())


def bin_search(page, pa):
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
    return a_count


for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    a_count = bin_search(P, A)
    b_count = bin_search(P, B)
    if a_count > b_count:
        print(f"#{tc} B")
    elif b_count > a_count:
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")
