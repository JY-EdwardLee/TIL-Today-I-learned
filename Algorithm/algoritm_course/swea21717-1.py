import sys
sys.stdin = open("input.txt", "r")


# 사람의 수 N, K번째 나열
n = int(input())
k = int(input())


def solution(n, k):
    arr = [num for num in range(1, n+1)]
    answer = None
    count = 0
    i = 0
    def f(i, n):
        nonlocal answer
        nonlocal count
        if i == n:
            print(arr)
            count += 1
            if count == k:
                answer = arr[:]
        else:
                for j in range(i, n):
                    arr.insert(i, arr.pop(i))
                    f(i+1, n)
                    arr.insert(j, arr.pop(i))
    f(i, n)
    return answer


print(solution(n, k))