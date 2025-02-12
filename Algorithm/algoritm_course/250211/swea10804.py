import sys
sys.stdin = open("../input.txt", "r")

T = int(input())


def mirroring(bdpq):
    N = len(bdpq)
    mirrored_word = ""
    for i in range(N-1, -1, -1):
        if bdpq[i] == 'p':
            mirrored_word += 'q'
        elif bdpq[i] == 'q':
            mirrored_word += 'p'
        elif bdpq[i] == 'b':
            mirrored_word += 'd'
        elif bdpq[i] == 'd':
            mirrored_word += 'b'
    return mirrored_word

for tc in range(1, T+1):
    bdpq = input()
    print(f'#{tc} {mirroring(bdpq)}')