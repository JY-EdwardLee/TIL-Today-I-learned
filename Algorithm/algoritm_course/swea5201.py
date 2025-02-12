import sys
sys.stdin = open("input.txt", "r")


T = int(input())


for tc in range(1, T+1):
    C, T = map(int, input().split())
    C_arr = list(map(int, input().split()))
    T_arr = list(map(int, input().split()))
    # 큰 화물부터 정렬
    T_arr.sort(reverse=True)
    C_arr.sort(reverse=True)
    total_volume = 0 # 최대 중량
    # 큰 화물부터 순회
    for i in range(T):
        # 큰 화물부터 최대 중량을 순회하면서 세팅
        volume = T_arr[i]
        # 빈자리가 최소화 되도록 채우기
        for j in range(C):
            # 감당 가능하면
            if volume - C_arr[j] >= 0:
                total_volume += C_arr[j]
                C_arr.pop(j)
                C_arr.append(0)
                break
    print(f'#{tc} {total_volume}')
