word = input("Enter a word: ")

vowels = ['a','e','i','o','u']
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
          found.append(letter)
print(found)