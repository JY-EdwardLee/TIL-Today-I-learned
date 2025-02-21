# set 자료형 my_set와 dict 자료형 my_dict가 주어진다. 
# my_set을 순회하여 얻은 값을 key로 하는 my_dict의 value를 출력한다. 
# 순회중에 얻은 key가 my_dict에 없다면 None이 출력되어야 한다. 
# get 메서드를 활용한다. 

# var 변수에 dict의 키로 사용 가능한 자료형을 할당한다. (문자열, 튜플 등) 
# my_dict에 var 변수를 key로 하는 value '변수로도 키 설정 가능' 문자열을 할당한다. 
# 변경된 my_dict를 출력한다. 

# 코드를 여러번 실행하며 출력 결과가 어떻게 달라지는지 확인한다.

my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for key in my_set:
    print(my_dict.get(key))

var = (1, 2, 3, 'A')
my_dict[var] = '변수로도 키 설정 가능'

print(my_dict)