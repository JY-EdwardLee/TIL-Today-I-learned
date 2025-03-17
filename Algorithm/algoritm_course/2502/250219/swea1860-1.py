from collections import deque

T = int(input())
for tc in range(1, T+1):
    # 예약자 N명, 소요시간 M, 생산량 K
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = deque(arr)
    possible = impossible = False
    sec = arr[0]
    Bascket = (sec // M) * K
    Machine = sec % M
    while True:
        Bascket += (((arr[0] - sec)+Machine)//M) * K
        Machine = (((arr[0] - sec)+Machine) % M)
        sec = arr[0]
        # if Machine == M:
        #     Bascket += K
        #     Machine = 0
        while arr[0] == sec:
            if Bascket <= 0:
                impossible = True
                break
            arr.popleft()
            Bascket -= 1
            if not arr:
                possible = True
                break
        if impossible:
            print(f'#{tc} Impossible')
            break
        if possible:
            print(f'#{tc} Possible')
            break

