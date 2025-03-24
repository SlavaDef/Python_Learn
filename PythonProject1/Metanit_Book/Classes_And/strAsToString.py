class Person11:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст

    def display_info(self):
        print(self)
        # print(self.__str__())     # или так

    def __str__(self):  # аналог toString
        return f"Name: {self.name}  Age: {self.age}"


tom = Person11("Tom", 23)
print(tom)  # Name: Tom  Age: 23
tom.display_info()  # Name: Tom  Age: 23