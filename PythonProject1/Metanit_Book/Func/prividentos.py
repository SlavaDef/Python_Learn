a = 'hi'
b = 'io'
c = 'niga'
d = a + ' '+ b + c

print(a,b,c)

print(d, sep=",")


word = 'Python is the interesting language in the word'

wordsList = list(word)
print(wordsList)

for i in word:
    print(i, end=' ')

for a in wordsList:
    print(a, end=' ')

w = '28'
s = '15'

h = int(w) + int(s)

print(h.__class__)

res = str(h)

print(res.__class__)