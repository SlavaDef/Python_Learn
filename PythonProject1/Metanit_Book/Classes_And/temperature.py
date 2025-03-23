# Базові методи встановлення та отримання атрибутів в Python
class Celsius:

    def __init__(self, temperature=0):
        self.__temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self.__temperature



# Створюємо новий об'єкт
human = Celsius(36.6)

# Встановлюємо температуру
#human.temperature = 36.6 # тепер доступ закритий, встановлення через сет

# Виводимо температуру в градусах за Цельсієм
print(human.temperature)

# Виконуємо конвертацію та виводимо температуру в градусах за Фаренгейтом
print(round(human.to_fahrenheit(),4))


class Celsius2:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # Метод-геттер
    def get_temperature(self):
        return self.__temperature

    # Метод-сеттер
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self.__temperature = value


# Створюємо новий об'єкт, викликається метод set_temperature()
human = Celsius2(37)

# Отримуємо атрибут температури за допомогою геттера
print(human.get_temperature())

#print(human.temperature) # до змінної доступу не має

# Виконуємо конвертацію температури в градуси за Фаренгейтом
print(human.to_fahrenheit())

# Реалізація нових обмежень
#human.set_temperature(-300) # викине ерор+++

# Виконуємо конвертацію температури в градуси за Фаренгейтом
print(human.to_fahrenheit())