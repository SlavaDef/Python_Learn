# Багаторядковий рядок використовуються тройні лапки
message = """
Never gonna give you up  
Never gonna let you down
"""
print(message)

word = 'never clever enough'
print(word[::-1]) # hguone revelc reven
print(word[6]) # but we can't do word[6] = '0' error
print()
str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# Порівняння рядків str1 та str2
print(str1 == str2)

# Порівняння рядків str1 та str3
print(str1 == str3)

words = ['never', 'clever', 'enough', 'clever','del', 'del', 'some', 'clever', 'some']
words2 = ['some','del', 'clever']
#result = set(words) & set(words2)
res = list(filter(lambda x: x in words2, words))

print(res)

print('a' in 'program')     # виведе True
print('at' not in 'battle') # виведе False

word66 = 'gogivashington'
new_word = word66.partition('iv') # ('gog', 'iv', 'ashington')
print(new_word)
# Замінює підрядок усередині рядка.
print(word66.replace('va','11')) # gogi11shington
word67 = 'fdffk*lgg*kkkgk*'
print(word67.rstrip('*')) # ???
new_word67 = word67.split('*') # ['fdffk', 'lgg', 'kkkgk', '']
print(new_word67)

# Екранування подвійних лапок
example = "He said, \"What's there?\""

# Екранування одинарних лапок
example2 = 'He said, "What\'s there?"'

print(example)

print(f'{word66} and another word {word67} and another word {str1}, {str2}') # форматування рядку замість конкатенації

