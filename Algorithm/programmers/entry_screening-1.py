
# n = 100000000
# times = list(range(1, 10000))
n = 6
times = [7, 10]
ma = max(times) * n
mi = 0
while mi < ma:
    ce = (ma + mi)//2
    temp = sum(ce//time for time in times)
    temp1 = sum((ce-1)//time for time in times)
    if temp1 < n <=temp:
        break
    if n > temp:
        mi = ce
    elif n <= temp:
        ma = ce

print(ce)