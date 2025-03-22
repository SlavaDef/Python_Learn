# [start:stop:step]
from http.cookiejar import join_header_words

phrase = "Don't panic!"
letters = list(phrase)
print(letters)
print(letters[0:10:3]) #шаг друкувіти кожну третю букву від 0 до 10(не включно
print(letters[3:]) # пропустити перші три далі надрукувати всі до кінця, початок 3 далі за замовчуванням ніби до макс шаг 1
print(letters[:10]) # oll letters to 10 ind
print(letters[::2]) # кожну другу

letters2 = letters[::2]
print(letters2)

words = ("Whatever they charge us, we're charging them': "
         "Trump pledges more EU tariffs in trade war")

words_list = list(words)
print(words_list[0:3]) # choose first three letters

new_phrase = "".join(words_list[0:3])
print(new_phrase)

new_phrase2 = "".join(words_list[-6:]) # choose last 6 letters
print(new_phrase2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers[::2]) # all odd numbers
print(numbers[1:21:2]) # all even numbers

print(words_list[::-1]) # reverse massive from last index to first
print("".join(words_list[::-1])) # join letters in massive

every_other = words_list[::2] # every other letter
print("".join(every_other))

print("".join(words[8:13])) # take word from 8 index to 13 index - they (cut out the word from massive)

print("".join(words[13:8:-1])) # take word from 8 index to 13 index  in reverse order