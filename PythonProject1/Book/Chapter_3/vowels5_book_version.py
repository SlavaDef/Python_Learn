word = input("Enter a word: ")

vowels = ['a','e','i','o','u']
#count_dictionary ={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
count_dictionary ={} # empty dictionary
for letter in word: # for every letter in word
    if letter in vowels: 
        count_dictionary.setdefault(letter,0) # another way of initialize dictionary
        count_dictionary[letter] += 1

for k, v in sorted(count_dictionary.items()):
    if v > 0: # if we dont wont to print letters with 0
       print(k, 'was found ', v, ' time(s)')