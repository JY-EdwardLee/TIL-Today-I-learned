'''
3
1 3 4 5 8 2 1 4 5 9 5
right
7 0 8 2 8 3 1 5 7 6 2
left
1 2 3 4 5 6 7 8 9 0
right
'''


def get_dist(s, e):
    arr = [[1,2,3],[4,5,6],[7,8,9],[10,0,12]]
    for y in range(4):
        for x in range(3):
            if arr[y][x] == e:
                e_p = y, x
            if arr[y][x] == s:
                s_p = y, x
    dist = abs(e_p[0] - s_p[0]) + abs(e_p[1] - s_p[1])
    return dist


def solution(numbers, hand):
    N = len(numbers)
    hand = hand.upper()
    left_f = 10
    right_f = 12
    answer = ''
    for i in range(N):
        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            left_f = numbers[i]

        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            right_f = numbers[i]

        else:
            l_dist = get_dist(numbers[i], left_f)
            r_dist = get_dist(numbers[i], right_f)
            if l_dist == r_dist:
                answer += hand[0]
                if hand[0] == 'R':
                    right_f = numbers[i]
                else:
                    left_f = numbers[i]
            elif l_dist > r_dist:
                answer += 'R'
                right_f = numbers[i]
            elif r_dist > l_dist:
                answer += 'L'
                left_f = numbers[i]
    return answer



T = int(input())
for _ in range(1, T+1):
    numbers = list(map(int, input().split()))
    hand = input().upper()
    left_num = [7, 4, 1]
    right_num = [9, 6, 3]
    center_num = [2, 5, 8, 0]
    answer = solution(numbers, hand)

    print(answer)

