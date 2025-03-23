def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return       # при цій умові друкуватись вік і імя не буде
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)


def say_hello(): print("Hello")


def say_goodbye(): print("Good Bye")


message = say_hello # змінній присвоїли функцію і потім викликали як функцію
message()  # Hello виклик змінної message()  як звичайної функції

message = say_goodbye
message()  # Good Bye


def summa(a, b): return a + b


def multiply(a, b): return a * b


operation = summa
result = operation(5, 6)
print(result)  # 11

operation = multiply
print(operation(5, 6))