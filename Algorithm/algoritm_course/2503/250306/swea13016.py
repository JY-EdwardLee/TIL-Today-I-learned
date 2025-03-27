#16진수를 2진수로 만드는 함수
def dec_to_bit(data):
    bit = [0] * 4	# 0000 ~ 1111이기 때문에 미리 [0, 0, 0, 0] 만들어 두기
    p = 3	# 인덱스 번호 (뒤에서 부터 이기 때문에 3)
    while int(data) > 0:	# 나누다가 0되면 멈추기
        bit[p] = int(data) % 2	# bit의 인덱스 번호에 나머지 넣기
        data = int(data) // 2	# 나누기
        p -= 1	# 인덱스 번호 1 낮추기
    return "".join(map(str, bit))	# 리스트를 str형식으로 반환

#16진수를 2진수로 만드는 함수
def hex_to_bit(data):
    global bits	# global bits
    # 아래는 인풋되는 값의 타입에 따라 변환 후 bits 변수에 추가하는 함수
    for num in data if type(data) is not int else [data]:	# int 형식의 data가 들어오면 [data], 그 외는 data 그대로 for loop 진행
        if type(num) is int or num not in 'ABCDEF': 	# num의 타입이 int이면 or 만일 num이 ABCDEF에 없으면
            bits += dec_to_bit(num)		# 10진수를 2진수로 변환하는 함수를 통해 변환 후 bits에 더해주기
        else:	# 알파벳이 들어오면
            alps = list(range(10, 16))	# [10, 11, 12 ,13 ,14, 15] 리스트 생성
            hex_to_bit(alps['ABCDEF'.index(num)])	# 'ABCDEF" str의 인덱싱을 통해 알파벳에 맞는 10진수 불러와서 재귀함수 진행

T = int(input())	# 테스트 케이스 개수

for tc in range(1, T+1):
    # hex_to_bit 함수 안에서 global bits 변수에 주어진 16진수를 한자리 씩 변환 할 예정
    bits = ''		# global bits 변수
    N, bin = map(str, input().split())	# 길이 N, 변수 bin
    hex_to_bit(bin)	# bits 변수에 2진수를 쌓는 함수
    print(f'#{tc} {bits}')