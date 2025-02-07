# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

def kill_paris(N, M):
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 토탈킬 디폴트 세팅
    total_kill = 0
    # MxM은 마지막 인덱스-M까지 순회
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for inc_i in range(0, M):
                for inc_j in range(0, M):
                    ni = i + inc_i
                    nj = j + inc_j
                    kill += arr[ni][nj]
            if kill > total_kill:
                total_kill = kill
    return total_kill


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    print(f'#{tc} {kill_paris(N, M)}')