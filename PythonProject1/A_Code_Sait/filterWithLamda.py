# Функція filter() приймає два параметри:

#    function — функція;
#    iterable — ітерований об’єкт, такий як множини, списки, кортежі тощо.


def check_even(number):
   # if number % 2 == 0:
     #   return True

   # return False
   return True if number % 2 == 0 else False # більш короткий запис якщо умови дві



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Якщо елемент, переданий у функцію check_even(), повертає True, вибираємо його
even_numbers_iterator = filter(check_even, numbers)

# Конвертуємо в список
even_numbers = list(even_numbers_iterator)
# чи так
even_numbers2 = list(filter(check_even, numbers))
print(even_numbers2)
print(even_numbers)
print()

with_lamda = list(filter(lambda x: x % 2 == 0, numbers))
print('Using lamda:', with_lamda)

print()


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


# Функція повертає True, якщо елемент є голосною літерою
def filter_vowels(letter): # пишемо метод для перевірки
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False


filtered_vowels = filter(filter_vowels, letters) # y фільтр передаємо метод пошуку і кортеж

# бистріші способи
filtered_list_vowels = list(filter(filter_vowels, letters))
#filtered_vowels = list(filtered_vowels)
# filtered_vowels = tuple(filtered_vowels)



# Конвертуємо в кортеж
vowels = tuple(filtered_vowels) # приводемо до кортеджу/множини/списку
print(vowels)

print('filtered list vowels with using lamda:',filtered_list_vowels)

# аналог знаходження проценту від числа за допомогою лямда
result = lambda x, y: x-( x*y/100 )
print(result(125,3))
# print(lambda x, y: x-( x*y/100)) # <function <lambda> at 0x00000222F8ED72E0> не вийде пише пургу
print()

# Випадковий перелік
random_list = [1, 'a', 0, False, True, '0']

filtered_list = list(filter(None, random_list)) # return only True

# Коли None використовується як перший аргумент функції filter(), вилучаються всі елементи,
# які є True (при перетворенні в логічні значення мають значення True).

print(filtered_list)