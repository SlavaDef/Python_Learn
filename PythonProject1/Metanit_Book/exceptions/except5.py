
x = None

while x is None: # поки х x is None помилка перехоплюється і відправляється знову у блок трай
    try:
        x = int(input("Enter a number of: "))
            #if x == 66: break
            #print(square(x))
        print(x*55) # як тільки х отримує якусь значення то цикл завершить роботу
        print(x)
        # x = None з цим полем вийде ніби безкінечний цикл
    except ValueError:
        print("You didn't enter a number")
       # x = int(input("Enter a number of month: "))
       # print(x * 55)
        #print(x)
    else:
        print("No errors") # якщо все спрацювало і помилок немає то це виведеться

    finally: # спрацює у будьякому випадку чи то при except чи після try
        print("This is the finally block")