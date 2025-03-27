import sys
sys.stdin = open("../../input.txt", "r")

def bin_search(arr, k):
    l, r = 0, len(arr)-1
    cnt = 0
    l_list, r_list = [-1], [-1]
    while l <= r:
        cnt += 1
        m = (l+r)//2
        if arr[m] == k:
            return True
        elif arr[m] < k :
            l = m + 1
            if l_list[-1] + 1 == cnt:
                return False
            l_list.append(cnt)
        elif arr[m] > k:
            r = m - 1
            if r_list[-1] + 1 == cnt:
                return False
            r_list.append(cnt)
    return False

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_A = sorted(list(map(int, input().split())))
    arr_B = sorted(list(map(int, input().split())))

    total = 0
    for key in arr_B:
        if bin_search(arr_A, key):
            total += 1

    print(f'#{tc} {total}')