class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year


    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if value.lower() == '':
            raise ValueError('Make cannot be empty')

        self._make = value

    @property
    def model(self):
        return self._model


    @model.setter
    def model(self, value):
        print('helo from model setter')
        if value.lower() == '':
            raise ValueError('Make cannot be empty')

        self._model = value


    @property
    def year(self):
        return self._year


    @year.setter
    def year(self, value):
        if value > 2026 or value < 1800:
            raise ValueError('Incorrect year')

        self._year = value

    def print_car(self):
        print(f"Марка: {self._make}\tмодель: {self._model}\tрік: {self._year}")
        print(self._make, self._model, self._year) # звернення не до змінної до сетеру



car = Car('BMW', '550i', 2018)
car.print_car()
#print(car.make, car.model, car.year)

car.make = 'Toyota' # chenge name, year and model зверення до сеттеру не до змінної
car.model = 'Corolla'
car.year = 2005
car.print_car()

car._model = 'Byggatti' #?
car.print_car()
