

try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)

except:
    print("Error: Denominator cannot be 0.")

try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[1])
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")


class InvalidAgeException(Exception): # робимо власний вийняток
    "Raised when the input value is less than 18"
    pass


# Потрібно вгадати це число
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")


class SalaryNotInRangeError(Exception):
    """Виняток, викликаний помилками у вхідному значенні salary

    Атрибути:
        salary -- значення salary, яке викликало помилку
        message -- пояснення помилки
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

#Тут ми перевизначили конструктор класу Exception, щоб він приймав наші власні користувацькі аргументи salary та message.

#Потім конструктор батьківського класу Exception викликається вручну з аргументом self.message за допомогою
# методу super(). Користувацький атрибут self.salary визначається для подальшого використання.