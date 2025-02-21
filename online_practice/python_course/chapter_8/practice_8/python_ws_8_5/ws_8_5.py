class Dog():
    sound = "댕댕"

    def __init__(self):
        super().__init__()

    def bark(self):
        print("댕댕!")

class Cat():
    sound = "냐옹"

    def __init__(self):
        pass

    def meow(self):
        print("야옹!")

class Pet(Dog, Cat):
    def __init__(self):
        pass

    def play(self):
        print("애완동물과 놀기")

    def make_sound(self):
        print(self.sound)

    def __str__(self):
        return f'애완완동물은 {self.sound}소리를 냅니다.'
    
print(Pet())