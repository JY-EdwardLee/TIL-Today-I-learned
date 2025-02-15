import random

for i in range(8*8 - 4):

    v, h, c = random.randint(1,8), random.randint(1, 8), 1 if i%2 == 0 else 2
    print(v, h, c, sep= ' ')