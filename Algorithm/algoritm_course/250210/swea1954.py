import sys
sys.stdin = open("../input.txt", "r")


T = int(input())


def snail(arr, n, num):
    # 달팽이를 순회할 인덱스 세팅
    i = 0
    j = 0
    cnt = num   # 인덱스에 추가될 숫자 세팅
    # 기저 조건 : 원소가 하나뿐인 배열 일시 cnt + 1을 입력 후 리턴
    if n == 1:
        cnt += 1
        arr[0][0] = cnt
        return arr
    # 유도 부분 : 배열의 외곽을 채우고 내부는 재귀를 통해 채움
    # NxN 배열의 상단 채우기
    while 0 <= j < n-1:
        cnt += 1
        arr[i][j] = cnt
        j += 1
    # NxN 배열의 우측 모서리 채우기
    while 0 <= i < n-1:
        cnt += 1
        arr[i][j] = cnt
        i += 1
    # NxN 배열의 하단 채우기
    if j == n-1 and i == n-1:
      while j != 0:
          cnt += 1
          arr[i][j] = cnt
          j -= 1
    # NxN 배열의 좌측 모서리 채우기
    while j == 0 and i == n-1:
        while i != 0:
            cnt += 1
            arr[i][j] = cnt
            i -= 1
    # 재귀 부분 : NxN 배열의 N이 3이상 일 시 내부 배열이 있기 때문에 내부 부분에서 재귀함수 동작
    if n >= 3:
        recursion = snail([arr[i][1:n - 1] for i in range(1, n - 1)], n - 2, cnt)   # 외곽을 제외한 배열의 장기 부분
        for i in range(1, n-1):
            for j in range(1, n-1):
                arr[i][j] = recursion[i-1][j-1] # arr 배열의 장기(1,n-1)을 재귀를 통해 도출한 배열로 채우기
    return arr


for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')
    for x in snail(arr, N, 0):
        print(' '.join(map(str, x)))