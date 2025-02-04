# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.increment_of_animal()

    @classmethod
    def increment_of_animal(cls):
        cls.num_of_animal += 1


class Dog(Animal):
    def __init__(self):
        super().__init__()\

class Cat(Animal):
    def __init__(self):
        super().__init__()

class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        print(f'동물의 수는 {cls.num_of_animal}마리 입니다.')


dog = Dog()
Pet.access_num_of_animal()
cat = Cat()
Pet.access_num_of_animal()
