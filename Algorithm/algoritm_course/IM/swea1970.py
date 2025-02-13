T = int(input())

for tc in range(1, T+1):
    N = int(input())
    extra_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    extra_index = [0]*8
    test_money = 0
    for i in range(8):
        if test_money + extra_list[i] <= N:
            while test_money + extra_list[i] <= N:
                test_money += extra_list[i]
                extra_index[i] += 1
            if test_money == N:
                break

    print(f"#{tc}")
    print(f"{' '.join(map(str, extra_index))}")

