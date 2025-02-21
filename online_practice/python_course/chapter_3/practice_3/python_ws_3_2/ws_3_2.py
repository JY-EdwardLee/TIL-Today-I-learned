number_of_people = 0


def increase_user():
    pass
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user(name, age, address):
    pass
    increase_user()
    user_info = {"이름" : name,
                 "나이" : age,
                 "주소" : address,
                 }
    print(f'{user_info["이름"]}님 환영합니다!')
    print(user_info)
    print(f'현재 가입 된 유저 수 : {number_of_people}')
    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')
create_user("홍길동", 30, "서울")