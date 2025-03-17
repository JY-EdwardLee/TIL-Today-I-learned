import sys
sys.stdin = open('../../input.txt', 'r')


T = int(input())


def gns(case):
    process = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    temp = [0] * len(case)
    count = [0] * 10

    for num in case:
        i = process.index(num)
        count[i] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for num in case[::-1]:
        i = process.index(num)
        count[i] -= 1
        temp[count[i]] = num
    return temp

for tc in range(1, T+1):
    number, N = map(str, input().split())
    case = list(map(str, input().split()))
    print(f'{number}')
    print(' '.join(gns(case)))