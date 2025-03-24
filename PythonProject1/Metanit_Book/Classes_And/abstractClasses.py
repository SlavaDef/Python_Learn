import abc # при створені абстракт класу треба унаслідуватися


class Shape(abc.ABC): # клас наслідується
    @abc.abstractmethod # абстракт метод наслідники всі повинні його реалізувати
    def area(self): pass  # площадь фигуры


# класс прямоугольника
class Rectangle(Shape):  # наслідуємося від фігури
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): return self.width * self.height # наслідник отже повинен реалізувати методи абстракт класу


# класс круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): return self.radius * self.radius * 3.14 # тут вже інша реалізація бо клас інший


def print_area(shape):
    print("Area:", shape.area()) # метод для друку


rect = Rectangle(30, 50)
сircle = Circle(10)
print("Rectangle area:", rect.area())  # Rectangle area: 1500
print_area(сircle)