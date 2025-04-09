# url : https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    sides.sort()
    for i in range(sides[1] - sides[0] + 1, sides[1]):
        answer += 1
    for i in range(sides[1], sum(sides)):
        answer += 1
    return answer

sides = [3, 6]
print(solution(sides))