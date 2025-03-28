from Gosha_Lessons.set_examples import result


# first method without arguments, method return how many times your letters was in your word
def find_letters_in_words_version_first():
    letters = list(input("Enter letters you would like to find in the word: "))
    word = input("Enter a word: ")
    count_dictionary = {}  # empty dictionary
    for letter in word:  # for every letter in word
        if letter in letters:
            count_dictionary.setdefault(letter, 0)  # another way of initialize dictionary
            count_dictionary[letter] += 1

    for k, v in sorted(count_dictionary.items()):
        print(k, 'was found ', v, ' time(s)')



def find_letters_in_words_version_second():
    # this method return letter that found in the word and it's count
        letters = input("Enter letters you would like to find in the word: ")
        word = input("Enter a word: ")

        count_dictionary = {}  # empty dictionary

        for letter in letters:
            count_dictionary[letter] = 0 # make dictionary with input letters(key) and value = 0
        for letter in word:  # for every letter in word
            if letter in letters:
               count_dictionary[letter] += 1

        for k, v in sorted(count_dictionary.items()):
                print(k, 'was found ', v, ' time(s)')



def find_letters_in_words_version_third(letters:str, phrase:str):
     res = sorted(set(letters).intersection(set(phrase))) # SET єто множество
     for letter in res:
       print(letter, ' - was been found in word' )







def counter(letters, phrase):
    # method to find count of letters in word/text return dictionary
    count_dictionary = {}  # empty dictionary

    for letter in letters:
        count_dictionary[letter] = 0  # make dictionary with input letters(key) and value = 0
    for letter in phrase:  # for every letter in word
        if letter in letters:
            count_dictionary[letter] += 1
    return count_dictionary



def find_letters_in_words_version_four(letters: str, phrase: str):
    #count_dictionary = counter(letters, phrase)
    res = sorted(set(letters).intersection(set(phrase)))  # SET єто множество
    for letter in res:
               print(letter, ' - was been found in word', counter(letters, phrase)[letter], 'times' )# or dictionary



#find_letters_in_words_version_second()
#find_letters_in_words_version_third('oiu','hollidays')

print(find_letters_in_words_version_four('oiu','holliiidays'))

