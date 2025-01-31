number_of_people = 0


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


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# user_profile = list(map(create_user, name, age, address))
user = zip(name, age, address)
print(user)
user_profile = list(map(lambda user : create_user(*user), user))
print(user_profile)