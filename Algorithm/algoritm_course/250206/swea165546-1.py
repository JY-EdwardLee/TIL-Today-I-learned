'''
10
123456
139673
644544
123123
667767
054060
101123
000000
111111
532235

'''
T = int(input())

def baby_gin(num):
    counts = [0]*11 # 0~9
    card_str = str(num)
    card = list(map(int, card_str))
    for i in range(6):
        counts[card[i]] += 1 # [0, 0, 0, 1, 4, 1, 0..]
    run_count = 0
    triplet= 0
    # triple 점검하기
    j = 0
    while j < 10:
        if counts[j] >= 3:
            counts[j] -= 3
            triplet += 1
        else:
            j += 1
    # run_count 점검하기
    i = 0
    while i < 10:
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run_count += 1
        else:
            i += 1
    if run_count + triplet == 2:
        return f'true'
    else:
        return f'false'

for tc in range(1, T+1):
    num = input().stip()
    print(f'#{tc} {baby_gin(num)}')