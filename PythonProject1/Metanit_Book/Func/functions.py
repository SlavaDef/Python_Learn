def say_hello():  print("Hello ", end="")



say_hello()
say_hello()

print("Bye")
print()

def print_messages():
    # определение локальных функций
    def say_hello2(): print("Hello")

    def say_goodbye(): print("Good Bye")

    # вызов локальных функций
    say_hello2()
    say_goodbye()


# Вызов функции print_messages
print_messages()

# say_hello() # вне функции print_messages функция say_hello не доступна
