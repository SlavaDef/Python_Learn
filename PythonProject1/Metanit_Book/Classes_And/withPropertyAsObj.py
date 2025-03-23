# Використання класу property
from Gosha_Lessons.decorators import Decorator, open_url2


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # Метод-геттер
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # Метод-сеттер
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # Створюємо об'єкт класу property
    # Будь - який код, який отримує значення temperature, автоматично викликає get_temperature() замість пошуку за
    # словником(__dict__).Аналогічно, будь - який код, який присвоює значення змінній temperature, буде автоматично
    # викликати set_temperature().

    temperature = property(get_temperature, set_temperature)

    # property(fget=None, fset=None, fdel=None, doc=None)
    # фактично це теж саме
    # Створюємо порожній property
    # temperature = property()

    # Присвоюємо fget
    # temperature = temperature.getter(get_temperature)

    # Присвоюємо fset
    # temperature = temperature.setter(set_temperature)


human = Celsius(37) # Setting value...

print(human.temperature)

print(human.to_fahrenheit())

# decor = Decorator(open_url2) # обьект класу декоратор відкриє сайт статті

#human.temperature = -300

# https://acode.com.ua/property-decorator-python/