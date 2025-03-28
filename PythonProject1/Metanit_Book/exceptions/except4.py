a = ["Зима", "Весна", "Літо","Осінь"]


def square(x=0):

   if x <= 2 or x == 12:
       return a[0]
   elif 3 <= x <= 5:
       return a[1]
   elif 5 < x <= 8:
       return a[2]
   elif 8 < x <= 11:
       return a[3]
   elif x > 12 or x < 0:
       return 'Error no such month in a year'


while True:

          try:
              x = int(input("Enter a number of month: "))
              if x == 66: break
              print(square(x))
          except ValueError:
              print("You didn't enter a number")


print("End of program")


