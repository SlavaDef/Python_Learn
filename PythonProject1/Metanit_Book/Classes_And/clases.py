class Person:

    def __init__(self, name, age): # звичайний конструктор
        self.name = name  # имя человека
        self.age = age  # возраст человека

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Tom", 22)
tom.display_info()  # Name: Tom  Age: 22

bob = Person("Bob", 43)
bob.display_info()  # Name: Bob  Age: 43



class Person2:

    def __init__(self, name): # конструктори з отступом інші методи без?
        self.name = name
        print("Створили людину з ім'ям", self.name)

    def __del__(self): print("Видалили людину з ім'ям", self.name)


def create_person():
    tom2 = Person2("Tom")
    print(tom2.name)


create_person()

print("Кінец програми")