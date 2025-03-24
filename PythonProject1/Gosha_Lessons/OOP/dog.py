from Gosha_Lessons.OOP.animal import Animal


class Dog(Animal):


   def display(self):
        # Доступ до атрибута name батьківського класу за допомогою self
        print("My name is ", self.name)
        print("I am ", self.age, " years old")
        print("i ap happy and it's", self.isHappy)

        super().eat() # визов батько класу





labrador = Dog() # create object
labrador.name = "Labrador"
labrador.age = 5
labrador.isHappy = True


labrador.eat() # father class


labrador.display()
print()
labrador.song()

