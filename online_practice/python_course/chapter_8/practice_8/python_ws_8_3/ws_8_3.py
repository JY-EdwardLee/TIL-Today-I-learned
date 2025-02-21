# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.increment_of_animal()

    @classmethod
    def increment_of_animal(cls):
        cls.num_of_animal += 1

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound

    def meow(self):
        print(self.sound)

cat1 = Cat("야옹")
cat1.meow()
