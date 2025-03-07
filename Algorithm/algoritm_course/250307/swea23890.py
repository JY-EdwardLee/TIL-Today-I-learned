pattern = ["001101","010011","111011","110001","100011",
            "110111","001011","111101","011001","101111"]
hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


T = int(input())

for tc in range(1, T+1):
    hexa_num = input().strip()
    password = []
    bins = ''
    for num in hexa_num:
        bins += hex_to_bin[num]
    end = int(len(bins) - bins[::-1].index('1'))
    while end > 6:
        password.append(pattern.index(bins[end-6:end]))
        end = end - 6
    password.reverse()
    print(f'#{tc} {" ".join(map(str, password))}')
