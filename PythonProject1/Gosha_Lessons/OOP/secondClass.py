from Gosha_Lessons.OOP.firstClass import Building
# інкапсуляція закриття певних полів для внутрішнього використання

class BusinessCenter(Building):

  __flour = None # по типу приватне поле


  def __init__(self, year, city, flour=50):
      super(BusinessCenter, self).__init__(year, city) # визов батькового конструктора
      self.flour = flour

      #print(f"The flour of construction is {self.flour}.")

  def get_info(self):
      super().get_info() # звернення до методу з головного класу
      print(f"The flour of construction is {self.flour}.")

  def get_flour(self):
      return self.__flour


  def display(self):
      print("This is a business center")



house = BusinessCenter(1990, 'Kyiv', 25)
house.get_info()
print()
house2 = BusinessCenter(1998, 'London', 44)
house2.get_info()
print()
hotell = BusinessCenter(2010, 'Ban-Koki')
hotell.get_info()
hotell.__year = 2015 # ні чого не змінеться бо поле закрите
hotell.get_info()
hotell.year = 2020
hotell.get_info() # але так всеодно змінеться
print()
print(hotell.get_flour())

