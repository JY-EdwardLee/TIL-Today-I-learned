
n = 6
times = [7, 10]
counter = [0] * (len(times))
times.sort()
time = 0

while n > 0 or set(counter) != {0}:
    time += 1
    for i in range(len(times)):
        if counter[i] == 0 and n > 0:
            counter[i] = 1
            n -= 1
        elif counter[i] != 0:
            counter[i] += 1
            if counter[i] == times[i]:
                counter[i] = 0
print(time)