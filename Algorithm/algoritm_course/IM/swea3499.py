import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def everyday_im_shuffling(arr,n):
    if n%2:
        half = n // 2 + 1
    else:
        half = n // 2
    shuffled_card = []
    for i in range(0, half):
        shuffled_card.append(arr[0:half][i])
        try:
            shuffled_card.append(arr[half:n][i])
        except IndexError:
            pass
    return shuffled_card

for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    print(f'#{tc} {" ".join(everyday_im_shuffling(arr, N))}')
