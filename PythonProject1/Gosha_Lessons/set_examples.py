# множини (Set) чимось схожі на кортеджи тільки ще + видаляються повтори, синтаксис {} , порядок не підтримується

# Створення порожньої множини
empty_set = set()
print('Data type of empty_set:', type(empty_set),'\n')

empty_set.add('Apple')
empty_set.add('Banana')
empty_set.add('Orange')

print(empty_set)

companies = {'Lacoste', 'Ralph Lauren'}

empty_set.update(companies) # метод update оновлює множину іншою множиною

print(empty_set)

empty_set.discard('Lacoste') # delete Lacoste

print(empty_set)

# мині задача є масив з якого треба видалити повтори

nums = {4, 8 ,5 ,4, 8, 5 ,22, 18, 4, 8, 5}

result = set(nums)  # метод set конвертує масив у множину
print(result)

new_nums = list(nums) # навпаки знову у список

print(new_nums)

# зі слова робимо множину

word = 'Hello world' #

print(set(word)) # {'e', ' ', 'o', 'w', 'l', 'd', 'H', 'r'}

dato = frozenset(['a', 'b', 'c',True,False,True]) # frozenset множина в якій немає методів для видалення, додавання, оновлення
print(dato)