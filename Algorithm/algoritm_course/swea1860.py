from collections import deque

T = int(input())
for tc in range(1, T+1):
    # 예약자 N명, 소요시간 M, 생산량 K
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 손님 오름차순 정렬
    arr.sort()
    # 덱에 넣기
    arr = deque(arr)
    # 초를 첫번째 손님으로 스킵
    sec = arr[0]
    # 생산된 붕어빵을 세팅
    Bascket = (sec//M)*K
    # 나머지
    Machine = sec%M
    possible = impossible = False
    while True:
        if Machine == M:
            Bascket += K
            Machine = 0
        while arr[0] == sec:
            if Bascket <= 0:
                impossible = True
                break
            arr.popleft()
            Bascket -= 1
            if not arr:
                possible = True
                break
        Machine += 1
        sec += 1
        if impossible:
            print(f'#{tc} Impossible')
            break
        if possible:
            print(f'#{tc} Possible')
            break

