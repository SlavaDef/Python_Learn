class Building:

    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city
        #self.get_info()


    def get_info(self):
        print(f"The year of construction is {self.year}.")
        print(f"The city of construction is {self.city}.")


