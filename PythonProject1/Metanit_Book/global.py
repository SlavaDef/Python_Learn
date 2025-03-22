name = "Tom"


def say_hi():
    global name # без цього поля ми не змінем глобальну
    name = "Bob"   # изменяем значение глобальной переменной
    print("Hello", name)


def say_bye():
    print("Good bye", name)


say_hi()  # Hello Bob
say_bye()  # Good bye Bob


def outer():  # внешняя функция
    n = 5

    def inner():  # вложенная функция

       # nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n) # 25

    inner()
    print(n) # 5


outer()  # 5
# 25    - inner
# 5     - outer