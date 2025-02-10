import sys
sys.stdin = open("input.txt", "r")


def ladder(arr):
    for start in range(100):
        h = start
        if arr[0][h]:
            i = 1
            while i < 99:
                if 0 < h < 99 :
                    if arr[i][h+1]:
                        while arr[i][h+1]:
                            if h == 98:
                                h =99
                                break
                            h += 1
                        i += 1
                    elif arr[i][h-1]:
                        while arr[i][h-1]:
                            if h == 0:
                                break
                            h -= 1
                        i += 1
                    else:
                        i += 1
                elif h == 0:
                    if arr[i][h+1]:
                        while arr[i][h+1]:
                            if h == 99:
                                break
                            h += 1
                        i += 1
                    else:
                        i += 1
                elif h == 99:
                    if arr[i][h-1]:
                        while arr[i][h-1]:
                            if h == 0:
                                break
                            h -=1
                        i += 1
                    else:
                        i += 1
            if arr[i][h] == 2:
                return start
        else: continue

for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{T} {ladder(arr)}')
