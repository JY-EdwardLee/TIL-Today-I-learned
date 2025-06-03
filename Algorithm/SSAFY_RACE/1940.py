# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do


T = int(input())
for tc in range(1, T+1):
    position = 0
    speed = 0
    commands = int(input())
    for _ in range(commands):
        inputs = input().split()
        try:
            command, accel = inputs
        except ValueError:
            command = inputs[0]
            accel = None
        if command == '0':
            position += speed
        elif command == '1':
            speed += int(accel)
            position += speed
        elif command == '2':
            speed -= int(accel)
            speed = speed if speed > 0 else 0
            position += speed
    print(f'#{tc} {position}')

"""
#1 3
#2 4
#3 15
#4 27
#5 38
#6 44
#7 240
#8 91
#9 48
#10 111
"""