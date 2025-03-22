person = dict(name="John", age=36, city="New York") # заповнення словника
print(person)

for key, value in person.items():
    print(key.upper() , ' is ', value)
    print(key.upper(),  value, sep=' : ') # sep вказує яким розділювачем розділяти змінні

for i in person.values():
    print(i) # print all values in dictionary

for i in person.keys():
        print(i)  # print all keys in dictionary

person.popitem() # delete last index
# person.pop("age") # delete by key
person['hobby'] = 'reading' # add new
print(person)