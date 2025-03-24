# Глобальна змінна
c = 1

def add():
    # Збільшуємо значення змінної c
    # c = c + 2 # не вийде змінити глобальну змінну

    print(c)


add()
 # рішенням буде обьявити змінну глобал

# Глобальна змінна
a = 1

def add2():
    # Використовуємо ключове слово global
    global a

    # Збільшуємо значення змінної c
    a = a + 2

    print(a)


add2() # значенн змінилося
print(a)


def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)


outer_function()
print("Outside both function: ", num)


# Тут ми оголосили змінну num як global всередині вкладеної функції inner_function().
# На змінну num у зовнішній функції outer_function() ключове слово global ніяк не впливає. 
# До та після виклику inner_function() змінна num є локальною змінною зі значенням 20,
# оскільки всі дії виконуються в локальній області видимості функції.
#
# А вже після завершення виконання функції outer_function() ми переходимо в глобальну область видимості,
# де змінна num приймає значення, визначене в функції inner_function(), тобто num = 25.
# Це пов’язано з тим, що ми використали ключове слово global.


