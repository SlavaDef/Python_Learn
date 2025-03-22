vowels = ['a','e','i','o','u']
found = {}

for letter in vowels:
    found[letter] = 0

print(found,'\n')
names = ['Pie', 'Apple', 'Pear','Banana','Orange','Mango']
fruits = {}

for name in names:
  fruits.setdefault(name,0)
print(fruits)