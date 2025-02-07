'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

'''
T = int(input())

def max_minus_min(arr_, N):
    max_num = arr_[0]
    min_num = arr_[0]
    for i in range(1, N):
        if arr_[i] > max_num:
            max_num = arr_[i]
        if arr_[i] < min_num:
            min_num = arr_[i]
    return max_num - min_num

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f"#{tc} {max_minus_min(arr, N)}")
