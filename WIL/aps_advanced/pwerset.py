

arr = list(range(1, 11))

for i in range(1<<len(arr)):
    subset = []
    temp = 0
    for j in range(len(arr)):
        if i & (1<<j):
             temp += arr[j]
             subset.append(arr[j])
             if temp > 10:
                 break
    else:
        if sum(subset) == 10:
            print(subset)


def dfs(cnt, total, subset):
    # 1. total이 10이면 출력해라
    if total == 10:
        print(subset)
        return

    # 2. total이 10을 넘으면 가지치기하자자
    if total > 10:
        return

    if cnt == 10:
        return

    dfs(cnt + 1, total + arr[cnt], subset + [arr[cnt]])
    dfs(cnt + 1, total, subset)

dfs(0, 0, [])