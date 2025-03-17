import sys
sys.stdin = open("../../input.txt", "r")


T = int(input())


def project_millionaire(arr, N):
    earned = 0
    start = 0
    # 최대 값 전까지 매일 1주씩 모으기
    while start < N:
        # 최대 값이 있는 index 탐색
        max_index = arr.index(max(arr[start:]))
        max_price = arr[max_index]
        # 최대 값 index에서 전부 매도
        earned += (max_price*(max_index-start) - sum(arr[start:max_index]))
        # 최대 값 다음 index에서 위 과정 반복
        start = max_index + 1
    return earned



for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {project_millionaire(arr, N)}')
