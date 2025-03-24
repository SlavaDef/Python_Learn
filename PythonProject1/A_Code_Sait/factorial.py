# Факторіал числа — це добуток всіх цілих чисел від 1 до вказаного числа.
# Наприклад, факторіал числа 6 дорівнює 1*2*3*4*5*6 = 720.
import math


def factorial(x):
    """Це рекурсивна функція
       знаходження факторіала цілого числа."""

    if x == 1:  # return (1 if x == 1 else x * factor(x - 1)) коротший запис
        return 1
    else:
        return (x * factorial(x - 1)) # функйфя визиває саму себе колись х буде 1 бо x-1 і if спрацює

factor2 = lambda x: 1 if x == 1 else x * factor(x - 1)

def factorial2(x): # аналог без рекурсії з циклом while
   res = 1
   while x > 1:
       res *= x
       x -= 1
   return res


def factor(x):  # аналог без рекурсії з циклом for
    result = 1
    for i in range(1, x+1):
        result *= x
        x-=1
    return result


num = 8
print("The factorial of", num, "is", factorial(num))
print("The factorial of", num, "is", factorial2(num))
print(factor(num))
print('with using lamda, the factorial of', num, "is",factor2(num))
print(math.factorial(num))



