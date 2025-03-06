import sys
sys.stdin = open("input.txt", "r")


def dec_to_bit(data):
    bit = [0] * 4
    p = 3
    while int(data) > 0:
        bit[p] = int(data) % 2
        data = int(data) // 2
        p -= 1
    return "".join(map(str, bit))

def hex_to_bit(data):
    global bits
    for num in data if type(data) is not int else [data]:
        if type(num) is int or num not in 'ABCDEF':
            bits += dec_to_bit(num)
        else:
            alps = list(range(10, 16))
            hex_to_bit(alps['ABCDEF'.index(num)])

T = int(input())

for tc in range(1, T+1):
    bits = ''
    N, bin = map(str, input().split())
    hex_to_bit(bin)
    print(f'#{tc} {bits}')