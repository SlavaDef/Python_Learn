# Використовуємо декоратор @property
# Дана реалізація проста та ефективна. Це рекомендований спосіб використання декоратора property.
class Celsius3:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# Створюємо об'єкт
human = Celsius3(37)

print(human.temperature)

print(human.to_fahrenheit())

# coldest_thing = Celsius3(-300) # error because of check

