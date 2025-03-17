import sys
sys.stdin = open("../input.txt", "r")

index_c = [(1, 0), (0, 1), (0, 0)]
index_d = [(1, 0), (1, 1), (0, 0)]


def easy_carrot(arr, N):
    so, joong, dae = arr[:N // 3], arr[N // 3:(N * 2) // 3], arr[(N * 2) // 3:N]
    while True:
        if len(so) > N // 2 or not joong:
            return -1
        if so[-1] == joong[0]:
            so.append(joong.pop(0))
        else:
            break
    while len(joong) < len(dae):
        joong.append(dae.pop(0))
    while True:
        if len(joong) > N // 2 or not dae:
            return -1
        if joong[-1] == dae[0]:
            joong.append(dae.pop(0))
        else:
            break
    if len(dae) > N // 2:
        return -1
    min_diff = max(abs(len(so) - len(joong)), abs(len(dae) - len(joong)), abs(len(so) - len(dae)))
    return min_diff

def pack_carrot(arr, N):
    min_min_d = N//5 + 1
    if N%3 == 1:
        for i, j in index_c:
            so, joong, dae = arr[:N//3 + i], arr[N//3 + i:(N*2)//3 + j + i], arr[(N*2)//3 + j + i:N]
            while True:
                if len(so) > N//2 or not joong:
                    return -1
                if so[-1] == joong[0]:
                    so.append(joong.pop(0))
                else:
                    break
            while len(joong) < len(dae) :
                joong.append(dae.pop(0))
            while True:
                if len(joong) > N//2 or not dae:
                    return -1
                if joong[-1] == dae[0]:
                    joong.append(dae.pop(0))
                else:
                    break
            if len(dae) > N // 2:
                return -1
            min_diff = max(abs(len(so) - len(joong)), abs(len(dae) - len(joong)), abs(len(so) - len(dae)))
            min_min_d = min(min_min_d, min_diff)
    elif N%3 == 2:
        for i, j in index_d:
            so, joong, dae = arr[:N//3 + i], arr[N//3 + i:(N*2)//3 + j], arr[(N*2)//3 + j:N]
            while True:
                if len(so) > N//2 or not joong:
                    return -1
                if so[-1] == joong[0]:
                    so.append(joong.pop(0))
                else:
                    break
            while len(joong) < len(dae) :
                joong.append(dae.pop(0))
            while True:
                if len(joong) > N//2 or not dae:
                    return -1
                if joong[-1] == dae[0]:
                    joong.append(dae.pop(0))
                else:
                    break
            if len(dae) > N // 2:
                return -1
            min_diff = max(abs(len(so) - len(joong)), abs(len(dae) - len(joong)), abs(len(so) - len(dae)))
            min_min_d = min(min_min_d, min_diff)
    else:
        min_min_d = easy_carrot(arr, N)
    return min_min_d
T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min_d = pack_carrot(arr, N)
    arr.sort(reverse=True)
    if pack_carrot(arr, N) != -1:
        min_d = min(min_d, pack_carrot(arr, N))
    print(f'#{tc} {min_d}')