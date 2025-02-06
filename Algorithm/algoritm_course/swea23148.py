import sys
sys.stdin = open("input.txt", "r")

# 노선 수 T
T = int(input())

def minimun_charge(arr, K, N, M):
    counts = [0] * (N+K) # 정류장 개수
    for i in range(M): # 
        counts[arr[i]] += 1 # counts = [0, 0, 1, 0, 0, 1, ...]
    moving = 0
    bus = 0
    while bus < N - K:
        if 1 in counts[bus:bus+K+1]:
            bus = len(counts[0:bus+K+1]) - (counts[bus:bus+K+1][::-1].index(1) + 1)
            moving +=1
        else:
            return 0
    return moving

for lane in range(1, T+1):
    # 최대 이동거리 K, 전체 정류장 개수 N, 충전기 설치된 정류장 개수 M
    K, N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    print(f'#{lane} {minimun_charge(arr, K, N, M)}')
