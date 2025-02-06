'''
3
5
49679
5
08271
10
7797946543

'''
T = int(input())

def count_card(num, N):
    counts = [0]*10 # 0~9까지 생성
    for _ in range(N):
        counts[num%10] += 1
        num //= 10
    max_index = 0
    for i in range(10):
        if counts[max_index] <= counts[i]:
            max_index = i
    return max_index, counts[max_index]

for tc in range(1, T+1):
    N = int(input())
    num = int(input())
    max_index, num_of_card = count_card(num, N)
    print(f'#{tc} {max_index} {num_of_card}')