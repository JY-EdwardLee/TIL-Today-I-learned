import sys
sys.stdin = open("../../input.txt", "r")


def typing(a, b):
    N = len(a)
    M = len(b)
    i = 0
    key_presses = 0

    while i < N:
        if a[i:i + M] == b:  # B를 사용할 수 있으면
            key_presses += 1  # 한 번의 키 입력으로 B 입력
            i += M  # B의 길이만큼 건너뜀
        else:
            key_presses += 1  # 한 글자 입력
            i += 1  # 다음 문자로 이동

    return key_presses


# 입력 처리
T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    print(f'#{tc} {typing(A, B)}')
