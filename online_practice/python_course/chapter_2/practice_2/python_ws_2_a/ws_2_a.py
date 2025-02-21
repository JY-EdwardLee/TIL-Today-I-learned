# 아래에 코드를 작성하시오.
"""
zero_list 변수에 숫자 0을 하나 가지고 있는 리스트를 할당한다. 
zero_list 변수를 출력한다. 
many_zero_list 변수에 숫자 0을 25만개 가지고 있는 리스트를 할당한다. 
단, 리스트와 곱셈 연산자를 활용하여 할당한다. 
many_zero_list의 길이를 출력한다. 
numbers 변수에 range를 활용하여 1부터 10까지의 수를 가진 리스트를 할당한다. 
numbers 변수를 출력한다. 
numbers의 3번째부터 마지막 요소까지 출력한다.
이때 각 n번째는 리스트의 index를 의미한다.
"""

zero_list = [0] # zero_list 생성
print(zero_list) # zero_list 출력

many_zero_list = zero_list*25000 # zero_lsit_many 생성
print(len(many_zero_list))

numbers = list(range(1,11)) 
print(numbers)
print(numbers[3:])
