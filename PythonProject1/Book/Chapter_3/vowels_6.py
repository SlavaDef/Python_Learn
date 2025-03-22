word = input("Enter a word: ")

#vowels = {'a','e','i','o','u'} # or vowels=set('aeiou')
vowels = set('aeiou')

found = sorted(vowels.intersection(word)) # work as for intersection in word find analog in vowels

#result = sorted(list(found2))

print(found,'\n')
#print(sorted(found)) # sort found2