

for _ in range(1, 11):
    tc = int(input())
    arr = []
    if _ in range(16):
        x = list(input())
        arr.append(x)
        if 2 in set(x):
            start = _, x.index(2)
