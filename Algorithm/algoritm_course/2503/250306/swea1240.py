import sys
sys.stdin = open("../../input.txt", "r")

Patter_list = ['0001101', '0011001', '0010011', '0111101', '0100011',
               '0110001', '0101111', '0111011', '0110111', '0001011']


def validation(keys):
    even = 0
    odd = 0
    for i in range(8):
        if (i+1)%2 == 1:
            odd += keys[i]*3
        else:
            even += keys[i]
    if (odd + even)%10 == 0:
        return 1
    else:
        return 0


def scanner(num):
    keys = []
    bin = 0
    while bin < len(num):
        bin_e = bin + 7
        keys.append(Patter_list.index(num[bin:bin_e]))
        bin = bin_e
    if validation(keys):
        return sum(keys)
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = 0
    for _ in range(N):
        line = input()
        if password:
            continue
        if '1' in set(line):
            end_p = M - line[::-1].index('1')
            password = line[end_p-56:end_p]
    print(f'#{tc} {scanner(password)}')

'''
#1 38 
#2 0 
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34
'''