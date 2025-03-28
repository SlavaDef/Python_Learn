# створення функції декоратора
def select(input_func):
    def output_func():  #  робимо функцію яка буде виконуватися замість оригінальної
        print("*****************")  # перед виводом ориг функції друк зірочок
        input_func()  # визов оригинальної функції фактично тут спрацьовує @select
        print("*****************")  # після виводу ориг функції друк зірочок

    return output_func  # повертаємо нову функцію


# функція яка буде виконуватися, оригінальна
@select  # применение декоратора select
def hello():
    print("Hello from ToKio")


# визов оригінальной функції
hello()

print()


def hello_world(): #  з @select бистріше але фактично можна просто передати функцію у функцію select і буде теж саме
    print("Hello World!")

select(hello_world)()