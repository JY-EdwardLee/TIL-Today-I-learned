import sys
sys.stdin = open("../input.txt", "r")


def palindrome(arr, memory):
    N = len(arr)
    for j in range(N, 1, -1): # 가장 긴 회문이 있는지 탐색하기 위해 길이 j 설정
        i = 0
        while i + j <= N:
            sent = arr[i:i+j]
            # 회문인지 확인
            if sent == sent[::-1]:
                length = len(sent)
                return length
            i += 1
        if memory > j:
            break
    return -1


for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    dist = 0
    max_dist = 0
    # 가로로 회문 탐색
    for i in range(100):
        dist = palindrome(arr[i], max_dist)
        max_dist = max(dist, max_dist)
    # 세로로 회문 탐색
    for j in range(100):
        j_arr = []
        for i in range(100):
            j_arr.append(arr[i][j])
        dist = palindrome(j_arr, max_dist)
        max_dist = max(dist, max_dist)
    print(f'#{tc} {max_dist}')