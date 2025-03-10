import sys
sys.stdin = open("../input.txt", "r")


def gukmin(arr):
    n = N * 0.37    # 퍼센트에 따른 인덱스 제한용 숫자(실수)
    i = N           # 인덱스 (1씩 내려갈 것)
    arr_2 = [0] * (N)   # 국민 셔플용 배열 만들기
    # 오버 핸드 셔플
    while i > n:
        i -= 1  # 인덱스를 뒤에서부터 하나씩해서 N*0.37보다 작아지면 멈추기
        arr.append(arr.pop(0))  # 앞에서 부터 하나씩 빼서 뒤에 추가
    # 퍼펙트 셔플
    for i in range(N//2 + N%2): # 짝수일 때, 홀수일 때 절반+1까지
        arr_2[i*2] = arr[:N//2 + N%2][i]    # 앞에 절반 0,2,4 ... 하나씩 추가ㅣ\
        try:
            arr_2[i*2 + 1] = arr[N//2 + N%2:][i]    # 뒤에 절반 1, 3, 5 하나씩 추가
        except IndexError:  # 만일 N이 홀수여서 너무 커지면 except
            pass # 패스
    return arr_2

T = int(input())

for tc in range(1, T+1):
    N, t = map(int, input().split())
    arr = list(range(1, N+1))
    for _ in range(t):
        arr = gukmin(arr)
    print(f"#{tc} {' '.join(map(str, arr))}")