import sys
sys.stdin = open("../../input.txt", "r")

def kakegurui(card, who):
    triplet = 0
    global Edward
    global Mosu
    if who == "Edi":
        cards = Edward
    else:
        cards = Mosu
    cards[card] += 1
    if 3 in cards:
        return who
    for i in cards:
        if i != 0:
            triplet += 1
            if triplet == 3:
                return who
        else:
            triplet = 0
    return 0

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    Edward = [0] * 10
    Mosu = [0] * 10
    for i in range(6):
        if kakegurui(arr[i*2], "Edi") == "Edi":
            print(f'#{tc} {"1"}')
            break
        if kakegurui(arr[i*2 + 1], "Ahn") == "Ahn":
            print(f'#{tc} {"2"}')
            break
    else:
        print(f'#{tc} {"0"}')
