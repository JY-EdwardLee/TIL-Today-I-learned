import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def serpentine_sort(arr, n):
    # 기저 조건
    if n == 1:
        return arr
    # OO 조건
    elif n%2 == 0:
        # 최대 디폴트 값 세팅
        maximum = 0
        # 최대값 구하기
        for i in range(1, n):
            if arr[i] > arr[maximum]:
                maximum = i
        arr[0], arr[maximum] = arr[maximum], arr[0]
        # return arr[:1] + serpentine_sort(arr[1:], len(arr[1:]))
        return arr[:1] + serpentine_sort(arr[1:], n-1)
    else:
        minimum = 0
        for i in range(1, n):
            if arr[i] < arr[minimum]:
                minimum = i
        arr[0], arr[minimum] = arr[minimum], arr[0]
        # return arr[:1] + serpentine_sort(arr[1:], len(arr[1:]))
        return arr[:1] + serpentine_sort(arr[1:], n-1)


for tc in range(1, T+1):
    # 배열의 길이 N 받음
    N = int(input())
    # 배열 arr 받음
    arr = list(map(int, input().split()))
    print(f'#{tc} {" ".join(map(str, serpentine_sort(arr, N)[:10]))}')