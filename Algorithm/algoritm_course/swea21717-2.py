# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque


# 사람의 수 N, K번째 나열
n = int(input())
k = int(input())


def solution(n, k):
    arr = deque([num for num in range(1, n+1)])
    answer = []
    count = 0
    i = 0
    def f(i, n):
        nonlocal answer
        nonlocal count
        if i == n:
            count += 1
            if count == k:
                answer
        else:
            for j in range(i, n):
                arr.rotate(1)
                f(i + 1, n)
                arr.rotate(-1)

    f(i, n)
    return answer


print(solution(n, k))