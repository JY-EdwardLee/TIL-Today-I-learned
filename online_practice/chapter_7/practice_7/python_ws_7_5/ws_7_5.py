# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

    def calculate_perimeter(self):
        return self.width*2 + self.height*2
    
    def print_info(self):
        print(f'Width: {self.width}',
              f'Height: {self.height}',
              f'Area: {Shape.calculate_area(self)}',
              f'Perimeter: {Shape.calculate_perimeter(self)}',
              sep = "\n")
    
    def __str__(self):
       return f'Shape: width={self.width}, height={self.height}'



shape1 = Shape(5, 3)
print(shape1)
