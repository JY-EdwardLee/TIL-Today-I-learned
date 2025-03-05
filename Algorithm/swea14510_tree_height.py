

def get_days(dist_arr, N):
    cnt = 0
    while len(set(dist_arr)) != 1:
        cnt += 1
        if cnt%2 == 1:
            for i in range(N):
                if dist_arr[i] == 0:
                    continue
                if dist_arr[i]%2 == 1:
                    dist_arr[i] -= 1
                    break
            else:
                if sum(dist_arr) == 2 and 1 not in dist_arr:
                    continue
                else:
                    for i in range(N):
                        if dist_arr[i] == 0:
                            continue
                        else:
                            dist_arr[i] -= 1
                            break
        else:
            for i in range(N):
                if dist_arr[i] != 0 and dist_arr[i] != 1:
                    dist_arr[i] -= 2
                    break
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    top_i = 0
    for i in range(N):
        if arr[i] > arr[top_i]:
            top_i = i
    dist_arr = [(arr[top_i] - t) for t in arr]
    result = get_days(dist_arr, N)
    print(f'#{tc} {result}')


'''
#1 0
#2 2
#3 1
#4 14
#5 4
#6 168
#7 17
#8 26
#9 32
#10 196
#11 404
#12 31
#13 36
#14 34
#15 363
#16 984
#17 55
#18 62
#19 62
#20 889
#21 1847
#22 71
#23 98
#24 94
#25 1892
#26 4172
#27 115
#28 132
#29 122
#30 3878
#31 344
#32 35
#33 42
#34 42
#35 462
#36 890
#37 47
#38 70
#39 62
#40 946
#41 1901
#42 89
#43 86
#44 96
#45 1977
#46 3591
#47 117
#48 134
#49 134
#50 3650
'''