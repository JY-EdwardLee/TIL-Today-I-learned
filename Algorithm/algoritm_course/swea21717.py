n = 3
k = 5
count = 0
def get_order(i, N, arr, k):
    global count
    result = None
    if i == N:
        count += 1
        if count == k:
            result = arr
            return result
    else:
        for j in range(i, N):
            arr[i], arr[j] = arr[j], arr[i]
            result = get_order(i+1, N, arr, k)
            arr[i], arr[j] = arr[j], arr[i]
            if result != None:
                return result

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    answer = get_order(0, len(arr), arr, k)

    return answer

print(solution(n, k))