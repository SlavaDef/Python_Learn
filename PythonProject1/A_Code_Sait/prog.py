result = lambda x, y: x-( x*y/100 )

print('Програма розраховує мінус процент від першого числа. 0 - це вихід')

while True:

    a = input("Введіть число: ")

    if int(a) == 0:
        print("На все добре до нових зустрічей!")
        break


    if not a.isdigit():
        print()
        print("Кривий ввід. Введіть число!")
        continue

    b = input("Введіть процент: ")
    if not b.isdigit():
        print()
        print("Кривий ввід. Введіть число!")
        continue

    a = int(a)
    b = int(b)

    print(result(a,b))
    print()