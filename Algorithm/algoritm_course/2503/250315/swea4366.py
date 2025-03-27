def btd(num):
    dec = 0
    for i in range(len(num)):
        dec += num[i]*(2**(len(num)-1-i))
    return dec

def ttd(num):
    dec = 0
    for i in range(len(num)):
        dec += num[i]*(3**(len(num)-1-i))
    return dec

def jungsik(num_2, num_3):
    for i in range(len(num_2)):
        k = num_2[i]
        num_2[i] = (num_2[i]+1)%2
        for j in range(len(num_3)):
            num_3[j] = (num_3[j]+1)%3
            if btd(num_2) == ttd(num_3):
                print(f'#{tc} {btd(num_2)}')
                return
            num_3[j] = (num_3[j] + 1) % 3
            if btd(num_2) == ttd(num_3):
                print(f'#{tc} {btd(num_2)}')
                return
            num_3[j] = (num_3[j] + 1) % 3
        num_2[i] = (num_2[i] + 1)%2


T = int(input())

for tc in range(1, T+1):
    num_2 = list(map(int,input()))
    num_3 = list(map(int,input()))
    jungsik(num_2, num_3)

