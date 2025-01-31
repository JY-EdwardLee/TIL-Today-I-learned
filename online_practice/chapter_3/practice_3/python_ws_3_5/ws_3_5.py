number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user(name, age, address):
    increase_user()
    user_info = {"이름" : name,
                 "나이" : age,
                 "주소" : address,
                 }
    print(f'{user_info["이름"]}님 환영합니다!')
    # print(user_info)
    return user_info

user = zip(name, age, address)
# print(user)
many_user = list(map(lambda user : create_user(*user), user))
# print(many_user)

def rental_book(info):
    user_data = info
    rental = user_data["나이"]//10
    decrease_book(rental)
    print(f'{user_data["이름"]}님이 {rental}권의 책을 대여하였습니다.')
    return rental


def decrease_book(rental):
    global number_of_book
    number_of_book -= rental
    print(f'남은 책의 수: {number_of_book}')
    return number_of_book

list(map(rental_book, many_user))