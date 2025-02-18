numbers = [4, 1, 2, 1]
target = 4
def solution(numbers, target):
    answer = 0
    v = 0
    visited = [0] * len(numbers)
    stack = []
    total = 0
    while True:
        if v == 0:
            if visited[v] == 0:
                visited[v] += 1
                stack.append(numbers[v]*1)
                v += 1
            elif visited[v] == 1:
                stack.pop()
                visited[v] += 1
                stack.append(numbers[v]*(-1))
                v += 1
            elif visited[v] == 2:
                break
        elif 0 < v < len(numbers) - 1:
            if visited[v] == 0:
                visited[v] += 1
                stack.append(numbers[v]*1)
                v += 1
            elif visited[v] == 1:
                stack.pop()
                visited[v] += 1
                stack.append(numbers[v]*(-1))
                v += 1
            elif visited[v] == 2:
                visited[v] = 0
                v -= 1
                stack.pop()
            # if abs(sum(stack) - target) > sum(numbers[v:]):
            #     stack.pop()
            #     v -= 1
        elif v == len(numbers) - 1:
            if visited[v] == 0:
                stack.append(numbers[v]*1)
                visited[v] += 1
                if sum(stack) == target:
                    answer += 1
            elif visited[v] == 1:
                stack.pop()
                visited[v] += 1
                stack.append(numbers[v] * (-1))
                if sum(stack) == target:
                    answer += 1
            elif visited[v] == 2:
                visited[v] = 0
                stack.pop()
                v -= 1



    return answer




print(solution(numbers, target))