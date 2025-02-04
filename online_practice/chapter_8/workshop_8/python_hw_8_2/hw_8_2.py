# 아래 함수를 수정하시오.
def check_number():
    try:
        number = int(input('숫자를 입력하세요 : '))
        if number > 0:
            print(f'양수입니다.')
        elif number == 0:
            print(f'0입니다.')
        else:
            print(f'음수입니다.')
    except ValueError:
        print(f'잘못된된 입력입니다.')


check_number()
