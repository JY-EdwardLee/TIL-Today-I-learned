import sys
sys.stdin = open("input.txt", "r")


pattern = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
           [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]

htb = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


def validation(code):
    valid = 0
    for i in range(len(code)):
        if i + 1 == 8:
            valid += int(code[i])
        elif (i+1)%2 == 1:
            valid += int(code[i])*3
        elif (i+1)%2 == 0:
            valid += int(code[i])
    else:
        if valid%10 == 0:
            return True
        else:
            return False



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())










































