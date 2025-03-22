class Computer:

    def __init__(self):
        self.__maxPrice = 900 # змінна закрита інші обьектита наслідники не мають доступу до неї

    def sell(self):
        #print("Selling Price: {}".format(self.__maxprice))
        print("Selling Price:", self.__maxPrice, "ye")

    def setMaxPrice(self, price):
        self.__maxPrice = price

# В цьому класі змінну можна змінити тільки через сеттер
c = Computer()
c.sell()

# Змінюємо ціну
c.__maxPrice = 1000
c.sell()

# Використовуємо функцію-сеттер
c.setMaxPrice(1000)
c.sell()
