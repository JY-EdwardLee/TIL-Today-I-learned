T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    data = input()
    # 30, 31
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    # 년/월/일 구분 (문자열 to int)
    YYYY = data[:4]
    MM = data[4:6]
    DD = data[6:8]
    YYYY_int = int(data[:3])
    MM_int = int(data[4:6])
    DD_int = int(data[7:9])
    if 0 < MM_int < 13:
        if MM_int == 2:
            if 1 <= DD_int <=28:
                print(f'#{test_case} {YYYY}/{MM}/{DD}')
            else:
                print(f'#{test_case} -1')
        elif MM_int in days_31:
            if 1 <= DD_int <= 31:
                print(f'#{test_case} {YYYY}/{MM}/{DD}')
            else:
                print(f'#{test_case} -1')
        elif MM_int in days_30:
            if 1 <= DD_int <= 30:
                print(f'{test_case} {YYYY}/{MM}/{DD}')
            else:
                print(f'#{test_case} -1')
    else:
        print(f'#{test_case} -1')
    # ///////////////////////////////////////////////////////////////////////////////////
