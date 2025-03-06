import sys
import decimal
sys.stdin = open('input.txt', 'r')


def dec_to_bit(dec):
    bit = ''
    i = -1
    while i > -14:
        if dec == 0:
            return bit
        else:
            if 2**i <= dec:
                bit += '1'
                dec -= 2**i
                i -= 1
            else:
                bit += '0'
                i -= 1
    return 'overflow'

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {dec_to_bit(N)}')