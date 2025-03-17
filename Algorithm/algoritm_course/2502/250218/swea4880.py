T = int(input())


def rsp(a, b):
    if a == 1 and b == 2:
        return b
    elif a == 2 and b == 3:
        return b
    elif a == 3 and b == 1:
        return b
    else:
        return a



def get_winner(number, N):
    if len(number) == 1:
        return number[0]
    elif len(number) == 2:
        if arr[number[0]] == rsp(arr[number[0]], arr[number[1]]):
            return number[0]
        else:
            return number[1]
    else:
        arr_1 = number[:(N+1)//2]
        w1 = get_winner(arr_1, len(arr_1))
        arr_2 = number[(N+1)//2:]
        w2 = get_winner(arr_2, len(arr_2))
        if arr[w1] == rsp(arr[w1], arr[w2]):
            return w1
        else:
            return w2

for tc in range(1,T+1):
    N = int(input())
    number = [num for num in range(0, N)]
    arr = list(map(int,input().split()))
    print(f'#{tc} {get_winner(number, N)+1}')
