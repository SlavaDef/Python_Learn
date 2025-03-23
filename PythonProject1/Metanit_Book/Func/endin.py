def outer():  # внешняя функция
    n = 5  # лексическое окружение - локальная переменная

    def inner():  # локальная функция
        nonlocal n
        n += 1  # операции с лексическим окружением
        print(n)

    return inner


fn = outer()  # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner

#fn()  # 6
#fn()  # 7
#fn()  # 8
#fn()  # 9
#fn()  # 10
#fn() # 11

for i in range(8):
     fn() # 6-13
    # outer() # nothing because function return another function

print()
def multiply(n):
    def inner(m): return n * m

    return inner # or return lambda m: n * m


fn2 = multiply(5) # fn = inner, так как функция outer возвращает функцию inner

print(fn2(5))  # 25
print(fn2(6))  # 30
print(fn2(7))  # 35