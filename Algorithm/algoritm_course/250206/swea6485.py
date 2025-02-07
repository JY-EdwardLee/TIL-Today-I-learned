import sys
sys.stdin = open("s_input (1).txt", "r")

T = int(input())

def count_bus(N):
    counts = [0] * 5001 # 1~5000
    for test_case in range(N):
        a, b = map(int,input().split())
        for i in range(a, b+1):
            counts[i] += 1
    P = int(input())
    bus_count = []
    for i in range(P):
        j = int(input())
        bus_count.append(counts[j])
    return bus_count

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {" ".join(map(str,count_bus(N)))}')