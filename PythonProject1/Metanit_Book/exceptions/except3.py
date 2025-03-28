class PersonAgeException(Exception): # генерація власного винятку
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age


    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        min_age, max_age = 1, 110
        if min_age < age < max_age:  # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else:  # иначе генерируем исключение
            raise PersonAgeException(age, min_age, max_age)


    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info()  # Имя: Tom  Возраст: 37

    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e)  # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 110