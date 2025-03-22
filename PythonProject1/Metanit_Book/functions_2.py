def summa(*numbers):  # якщо не знаємо скільки параметрів може буть, *numbers безкінечні парами
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")



def printing(*words): # скільки слів передаси стільки надрукує

    for word in words:
        print(word, end=" ")






def result_function(): # функція яка запускає інші функції
    summa(1, 2, 3, 4, 5)  # sum = 15
    summa(3, 4, 5, 6)
    printing("Hello", "world!", "in ", "our,", "country")


result_function()
