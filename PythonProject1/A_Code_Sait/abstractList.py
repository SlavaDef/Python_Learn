h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

# analog

h_letters2 = [ letter for letter in 'human' ]
print( h_letters2)

# analog
letters = list(map(lambda x: x, 'human'))
print(letters)

# Умови в абстракції списків
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
# виконується додавання в лист при виконанні двох умов
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
# виконується додавання в лист при виконанні двох умов
num_list2 = [y for y in range(100) if y % 5 == 0 if y % 3 == 0]
print(num_list2)
# Тут абстракція списків перевіряє 10 чисел від 0 до 9. Якщо i ділиться на 2, то в список obj додається Even.
# Якщо ні, то додається Odd.
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)