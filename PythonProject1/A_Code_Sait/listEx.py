import random

# Множина голосних
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(list(vowel_set))

# Словник голосних
vowel_dictionary = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print(list(vowel_dictionary)) # з словника витягне ключі

print()

# Виводимо випадкове число з діапазону від 10 до 20
print(random.randrange(10, 20))

# Створюємо список елементів
list1 = ['a', 'b', 'c', 'd', 'e']

# Виводимо випадковий елемент із списку list1
print(random.choice(list1))

# Перемішуємо список list1
random.shuffle(list1)

# Виводимо перемішаний список list1
print(list1)

# Виводимо випадкове число
print(random.random())

numbers = [number * number for number in range(1, 6)]

print(numbers)