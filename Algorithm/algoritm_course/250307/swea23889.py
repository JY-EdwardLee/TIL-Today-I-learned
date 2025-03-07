alps = ['A', 'B', 'C', 'D', 'E', 'F']
T = int(input())

for tc in range(1, T+1):
    hexa_num = input().strip()
    bin_list = ''
    for i, num in enumerate(hexa_num):
        try:
            bin_list += ('0000' + str(bin(int(num)))[2:])[-4:]

        except ValueError:
            t_num = alps.index(num) + 10
            bin_list += str(bin(int(t_num)))[2:]
    b = 0
    dec_list = []
    while b < len(bin_list):
        dec_list.append(int(bin_list[b:b+7], 2))
        b += 7
    print(f'#{tc} {" ".join(map(str, dec_list))}')