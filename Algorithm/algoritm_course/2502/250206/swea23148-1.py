import sys
sys.stdin = open("../../input.txt", "r")

# 노선 수 T
T = int(input())

def minimun_charge(arr, K, N, M):
    bus = 0
    moving = 0
    while bus < N - K:
        if :
            bus = charger
            moving += 1
        else:
            return 0
    return movingq

for lane in range(1, T+1):
    # 최대 이동거리 K, 전체 정류장 개수 N, 충전기 설치된 정류장 개수 M
    K, N, M = map(int, input().split())
    arr = set(map(int,input().split()))
    print(f'#{lane} {minimun_charge(arr, K, N, M)}')


