import sys
sys.stdin = open("input.txt", "r")


# 사람의 수 N, K번째 나열
n = int(input())
k = int(input())
arr = [num for num in range(1, n+1)]


def solution(n, k):
    answer = None
    i = 0
    count = 0
    def f(i, n):
    if i == n:
        return
        for j in range(n):
            arr[i], arr[j] = arr[j], arr[i]






    print(answer)


solution(n, k)