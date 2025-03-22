a = 0

#a = int(input("Write please number "))
while a != 66:
    a = int(input("Write please number "))

    if a > 10:
       print("a > 10, a =",a)
    elif a < 0:
       print("a < 0, a =",a)
    elif a > 0:
       print("a > 0, a =",a)
    else:
       print("Something wrong, a =",a)

print("You number is 66, Congratulates!!!")