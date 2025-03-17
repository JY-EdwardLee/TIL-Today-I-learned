import sys
sys.stdin = open("input.txt", "r")


def ladder(arr):
    for start in range(100):
        h = start
        if arr[99][h] == 2:
            i = 98
            # i 가 도착하기 전까지
            while 0 <= i < 99:
                # h가 내부일 때
                if 0 < h < 99 :
                    if arr[i][h+1]:
                        while arr[i][h+1]:
                            if h == 98:
                                h = 99
                                break
                            h += 1
                        i -= 1
                    elif arr[i][h-1]:
                        while arr[i][h-1]:
                            if h == 0:
                                break
                            h -= 1
                        i -= 1
                    else:
                        i -= 1
                # h가 좌측 모서리 일 때
                elif h == 0:
                    if arr[i][h+1]:
                        while arr[i][h+1]:
                            if h == 99:
                                break
                            h += 1
                        i -= 1
                    else:
                        i -= 1
                # h가 우측 모서리 일 때
                elif h == 99:
                    if arr[i][h-1]:
                        while arr[i][h-1]:
                            if h == 0:
                                break
                            h -=1
                        i -= 1
                    else:
                        i -= 1
            return h
        else:
            continue


for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    print(f'#{T} {ladder(arr)}')
