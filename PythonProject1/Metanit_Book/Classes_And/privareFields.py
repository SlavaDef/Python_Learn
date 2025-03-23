class Person3:



   def __init__(self, name, age):
        self.__name = name # __name в конструкторі закриваємо змінну щоб її не можна було змінити
        self.__age = age




   def print_person(self):
        print('The name is:', self.__name, '\nThe age is:', self.__age)




timmi = Person3("Timmi", 39)

timmi.__name = "Человек-паук"  # пытаемся изменить атрибут __name
timmi.__age = -129  # пытаемся изменить атрибут __


timmi.print_person() # Имя: Tom        Возраст: 39


timmi._Person3__name = "Человек-паук" # але зная назву атребутів через клас можна змінити
timmi.print_person()

bob = Person3("Bob", 25)
bob.name = "Bib" # не змінеться
bob.print_person()

#print(tom3.__age)