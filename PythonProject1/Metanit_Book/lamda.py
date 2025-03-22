message = lambda: print("hello") # створення  наче методу за допомогою лямди

message()  # hello

square = lambda n: n * n # лямда функція для знагодження числа

print(square(4))  # 16
print(square(5))  # 25

sum = lambda a, b: a + b

print(sum(4, 5))  # 9
print(sum(5, 6))  # 11


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


do_operation(5, 4, lambda a, b: a + b)  # result = 9
do_operation(5, 4, lambda a, b: a * b)  # result = 20


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60