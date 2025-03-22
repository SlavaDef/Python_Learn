class Robot:

    def __init__(self, name="Robot", model='new version', year=2025): # constructor
       # self.name = name
       # self.model = model
       # self.year = year
       # print('Name = ', self.name, ', model = ', self.model, ', created in ', self.year)
        self.set_data(name, model, year) # another way of creating
        self.get_data()



    def __init__(self, name=None, model=None, year=None): # empty constructor
        if name is None or model is None or year is None:
           print('Object without parameters has been created!')
        else:
            #self.name = name
            #self.model = model
            #self.year = year
            self.set_data(name, model, year)  # another way of creating
            self.get_data()



    def get_data(self):
        print('Name = ', self.name, ', model = ',self.model,', created in ', self.year)


    def set_data(self, name, model, year=2000): # year = 2000 парам за замовчуванням
        self.name = name
        self.model = model
        self.year = year

    #def __str__(self):
       # return f"Robot: {self.name}, {self.model}, {self.year}"


robot1 = Robot("Garry", "Robo 1", 2000)
robot2 = Robot("Bob", "Robo 2", 2001)
robot3 = Robot("Sonia", "Robo 3", 2002)
robot4 = Robot("Jane", "Robo 4", 2003)
robot5 = Robot()
robot6 = Robot(model='perfecto') # все за замовчуванням крім model його ми захотіли вкозати
robot7 = Robot()

#robot1.get_data()
#robot3.get_data()
print()
#robot4 = Robot()
#robot4.set_data("Garry", "Robo 1", 2000)
#robot4.get_data()

#robot5 = Robot()
robot3.set_data("Sindel", "Robo 3", 2005) # can enter 3 param
robot4.set_data("Jane2", "Robo 4") # or can enter 2 param
robot3.get_data()
robot4.get_data()



