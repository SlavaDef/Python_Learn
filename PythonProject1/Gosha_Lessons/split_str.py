word = "football,basketball,tennis "

hobbies = word.split(",") # make list from 3 elements

for i in range(0,len(hobbies)):
    hobbies[i] = hobbies[i].capitalize() # make big letters

result = ",".join(hobbies)
print(result)