# Множина цілочисленного типу
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# Множина рядкового типу
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# Множина змішаного типу
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
print()
# Створення порожньої множини
empty_set = set()

# Створення порожнього словника
empty_dictionary = {}

# Перевірка типу даних empty_set
print('Data type of empty_set:', type(empty_set))

# Перевірка типу даних dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
print()

# В Python метод update() використовується для оновлення множини елементів інших типів даних (списки, кортежі тощо)
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)

print(companies)
print()

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:', languages)

# Видалення 'Java' з множини
removedValue = languages.discard('Java')

print('Set after remove():', languages)
print()
# Перша множина
A = {1, 3, 5}

# Друга множина
B = {0, 2, 4}

# Виконання операції об'єднання за допомогою |
print('Union using |:', A | B)

# Виконання операції об'єднання за допомогою union()
print('Union using union():', A.union(B))