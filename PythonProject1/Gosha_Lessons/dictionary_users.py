peoples = {
    'user_1' : { # dictionary in dictionary
        'name' : 'John',
        'age' : 30,
        'address' : ('Kyiv', 'St.Konovalovaya', 66), # cortage
        'grades' : {'math' : 90, 'english' : 100, 'physics' : 80}

},
    'user_2' : {
        'surname' : 'Smith',
        'age' : 25
    }


}

print(peoples['user_1']) # get all info about user_1
print(peoples['user_1']['name']) # get only name about user_1 (John)
print(peoples['user_1']['address'][1]) # get first index in address (St.Konovalovaya)
print(peoples['user_1']['grades']['english']) # get english grades in grades ( 100 )