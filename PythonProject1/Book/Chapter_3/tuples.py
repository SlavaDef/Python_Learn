numbers = [55,22,55,99,77,66,66,22,77]

print(numbers)
word = 'hello'
t = {1,2,3} # множиство

t.add(6)
t.add(1)


print(t)


vowels = set('aeiouuuaa')
print(vowels)

u = vowels.union(set(word)) # ending only 2 letters
d = vowels.difference(set(word)) # відмінність
n = vowels.intersection(set(word))

print(u)
print(d) # відмінність
print(n)