# 노선 수 T
T = int(input())

def minimun_charge(arr, K, N, M):
    counts = [0] * N # 정류장 개수
    for i in range(M):
        counts[arr[i]] += 1



for lane in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int,input().split()))
