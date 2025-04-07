# url : https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [-1, 52, -1, 0]
    for i, line in enumerate(wallpaper):
        if '#' in line:
            if answer[0] == -1:
                answer[0] = i
            if answer[2] < i + 1:
                answer[2] = i + 1
            if line.find('#') < answer[1]:
                answer[1] = line.find('#')
            if len(line) - line[::-1].find('#') > answer[3]:
                answer[3] = len(line) - line[::-1].find('#')
    return answer

