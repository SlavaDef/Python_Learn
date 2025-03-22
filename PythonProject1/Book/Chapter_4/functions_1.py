


def vowel_finder():
    vowels = set('aeiou')
    word = input('Enter a word: ')
    found = sorted(vowels.intersection(word)) # work as for intersection in word find analog in vowels

    return found

def vowel_finder2():
    # print vowels(гласні)  in inputing word
    vowels = set('aeiou')
    word = input('Enter a word: ')
    found = sorted(vowels.intersection(word)) # work as for intersection in word find analog in vowels
    for letter in found:
        print(letter)

def vowel_finder_3(word_3):
            vowels = set('aeiou')
            found = sorted(vowels.intersection(word_3))
            for letter in found:
              print(letter)


def vowel_finder_4(word_3):
    s = False
    vowels = set('aeiou')
    found = sorted(vowels.intersection(word_3))
    if len(found) > 0:
        s = True
    return s

def vowel_finder_5(word_3):
# return True or false
    vowels = set('aeiou')
    found = sorted(vowels.intersection(word_3))

    return bool(found) # bool(object) return False if object is ampty or < 0 and True if object > 0

def vowel_finder_6(word_3:str) -> set:
    # return tuples
    vowels = set('aeiou')
    return vowels.intersection(word_3)

def vowel_finder_7(phrase, letters) :
    vowels = set(letters)
    return vowels.intersection(phrase)

def vowel_finder_8() :
    letters = input('Enter a set of letters: ')
    phrase = input('Enter a phrase: ')
    vowels = set(letters)
    return vowels.intersection(phrase)

def search_for_letters():
    letters = input('Enter a set of letters: ')
    result = set(letters)
    return result

def finder():
    letters = search_for_letters()
    phrase = input('Enter a phrase: ')
    return letters.intersection(phrase)

def finder2(letters:str, phrase:str):
    return letters.intersection(phrase)

def finder3(letters:str, phrase:str):
    return set(letters).intersection(set(phrase)) # SET єто множество


#vowel_finder2()
#print(vowel_finder_4(input('Enter a word: ')))
#print(vowel_finder_8())
#print(finder())
#print(finder2(search_for_letters(), input('Enter a phrase: ')))
#print(finder3(input("Enter letters"), input('Enter a phrase: ')))
for letter in finder3('aeiou', 'hello'):
   print(letter, ' - was been found in word' )


#print(finder3('aeiou', 'hello'))