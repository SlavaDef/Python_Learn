def summa(*numbers):  # якщо не знаємо скільки параметрів може буть, *numbers безкінечні парами
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")



def printing(*words): # скільки слів передаси стільки надрукує

    for word in words:
        print(word, end=" ")



def check():
    n = int(input('Enter len of list: '))
    numbers = []
    res = []
    for i in range(n):
       numbers.append(int(input()))
       if numbers[i] % 2 == 0:
           res.append(numbers[i])
    print(res)

    

def check2(*numbers):  # ніби створюється масив, не знаємо що передасть юзер

    for i in range(len(numbers)):

       if numbers[i] % 2 == 0:

          print(numbers[i])





def result_function(): # функція яка запускає інші функції
    summa(1, 2, 3, 4, 5)  # sum = 15
    summa(3, 4, 5, 6)
    printing("Hello", "world!", "in ", "our,", "country")
    print()
    check2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


result_function()

#check()






