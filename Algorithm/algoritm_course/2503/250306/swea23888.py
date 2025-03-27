import sys
sys.stdin = open("../../input.txt", "r")


def bit_to_dec(data):
    result = 0
    for i, num in enumerate(data[::-1]):
        result += int(num)*(2**i)
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = []
    bits = ''
    for _ in range(N):
        bits += input().strip()
    bin = 0
    while bin < len(bits):
        bin_e = bin + 7
        ans.append(bit_to_dec(bits[bin:bin_e]))
        bin = bin_e

    print(f'#{tc} {" ".join(map(str, ans))}')