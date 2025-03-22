from itertools import count

word = input("Enter a word: ")

vowels = ['a','e','i','o','u']
found = []
count = 0
count_dictionary ={'a':count, 'e':count, 'i':count, 'o':count, 'u':count}

for letter in word:
    if letter in vowels:
        count = count + 1
        count_dictionary[letter] += count
        count = 0
        if letter not in found:
          found.append(letter)

print(found)
print(count_dictionary)

for i in sorted(count_dictionary): # sorted make sort (only copy) from a to u, from 1 to 10
   print(i,'was found ',count_dictionary[i],' times')

print()
for k,v in sorted(count_dictionary.items()): # the same
    print(k,'was found ',v,' times')
