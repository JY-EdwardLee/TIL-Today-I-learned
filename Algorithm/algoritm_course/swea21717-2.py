# import sys
# sys.stdin = open("input.txt", "r")


# 사람의 수 N, K번째 나열
n = int(input())
k = int(input())


def solution(n, k):
    arr = [num for num in range(1, n+1)]
    answer = []
    count = 0
    i = 0
    p = [0] * n
    used = [0] * n
    def f(i, N):
        nonlocal count
        if i == N:  # p[i]를 모두 채운 경우
            count += 1
            if count == k:
                return p
        else:
            for j in range(N):  # 아직 p에 사용하지 않은 숫자를 찾아
                if used[j] == 0:
                    p[i] = arr[j]
                    used[j] = 1  # arr[j] 사용
                    result = f(i + 1, N)
                    if result:
                        return result
                    used[j] = 0  # arr[j]를 다른 자리에서 사용할 수있도록 함

    answer = f(i, n)
    return answer


print(solution(n, k))