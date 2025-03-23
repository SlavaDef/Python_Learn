class Person4:


    def __init__(self, name, age):
        self.__name = name  # встановлення имя
        self.__age = age  # встановлення возраст

    # сеттер для встановлення віку
    def set_age(self, age):
        if 0 < age < 110: # цікава перевірка на роки
            self.__age = age
        else:
            print("Incorrect age")

    # сеттер для встановлення імені
    def set_name(self, name):
        if name=="" or name ==" ":
            print("Incorrect name")
        else:
            self.__name = name

    # геттер для отримання віку
    def get_age(self):
        return self.__age

    # геттер для отримання імені
    def get_name(self):
        return self.__name

    def print_person(self):
        print(f"Імя: {self.__name}\tРочки: {self.__age}")


tom = Person4("Tom", 39)
tom.print_person()  # Имя: Tom  Возраст: 39

tom.set_age(-3486)  # Недопустимый возраст
tom.set_age(25)
tom.set_name("")
tom.set_name("Tom_2")

tom.print_person()  # Имя: Tom  Возраст: 25