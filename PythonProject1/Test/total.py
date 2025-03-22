total = 0

number = int(input('Enter a number: '))

# Додаємо числа, доки number не дорівнюватиме 0
while number != 0:
    total += number  # total = total + number

    # Запитуємо користувацький ввід
    number = int(input('Enter a number: '))

print('total =', total)