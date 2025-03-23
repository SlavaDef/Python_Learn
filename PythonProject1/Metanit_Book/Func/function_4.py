# Функция как параметр функции


def do_operation(a, b, operation):
    result = operation(a, b) # результат операції над двома змінними, якої опереції не відомо
    print(f"result = {result}")


def summa(a, b): return a + b


def multiply(a, b): return a * b


do_operation(5, 4, summa)  # result = 9 # цікаво в параметрии методу передаємо функцію
do_operation(5, 4, multiply)  # result = 20


def subtract(a, b): return a - b


def select_operation(choice):
    if choice == 1:
        return summa
    elif choice == 2:
        return subtract
    else:
        return multiply


operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60