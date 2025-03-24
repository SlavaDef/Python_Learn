class Person:
    type = "Person"

    def __init__(self, name):
        self.name = name


tom = Person("Tom")
bob = Person("Bob")
print(tom.type)  # Person
print(bob.type)  # Person

# изменим атрибут класса
Person.type = "Class Person"
print(tom.type)  # Class Person
print(bob.type)  # Class Person

print()
class Person9:
    default_name = "Undefined" # defolt name

    def __init__(self, name='Bobby'): # якщо взагалі не передати то буде за замовчуванням 'Bobby' чи вже блок else:
        if name:
            self.name = name
        else:
            self.name = Person9.default_name # створюємо змінну ніби і дефолтно присвоюємо імя якщо не передане


tom = Person9("Tom")
bob = Person9('')
jones = Person9()

print(tom.name)  # Tom
print(bob.name)  # Undefined
print(jones.name) # Bobby
print()

class Person10:
    name = "Undefined" # задали ніби імя за замовчуванням

    def print_name(self):
        print(self.name)


tom = Person10()
bob = Person10()
tom.print_name()  # Undefined
bob.print_name()  # Undefined

bob.name = "Bob"
bob.print_name()  # Bob
tom.print_name()  # Undefined