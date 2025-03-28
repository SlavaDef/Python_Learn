try:
    number = int(input("Введите число: "))
    print("Введенное число:", number)
except ValueError:
    print("Преобразование прошло неудачно")


print("Завершение программы")


try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1/number2)
except ValueError: # опрацює при введенні не числа ( не int)
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except BaseException: # опрацює любий інший вийняток
    print("Общее исключение")
print("Завершение программы")



try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    print("Результат деления:", number1 / number2)
except (ZeroDivisionError, ValueError):  # обработка двух типов исключений - ZeroDivisionError и ValueError
    print("Попытка деления числа на ноль или некорректный ввод")

print("Завершение программы")