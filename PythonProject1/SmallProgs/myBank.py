import json
import time

FILENAME = "bank_data.json"

# Спроба завантажити дані з файлу, якщо він існує
try:
    with open(FILENAME, "r") as f:
        bank = json.load(f)
except (FileNotFoundError, json.JSONDecodeError): # якщо файлу немає чи помилка читання загрузиться дефолтний словник
    bank = {'USD': 10927, 'EUR': 3800, 'GBP': 30, 'GRN': 30}

print("Початковий баланс:", bank)

currencies = ['USD', 'EUR', 'GBP', 'GRN']

while True:
    try:
        selection = int(input("Виберіть валюту (1-USD, 2-EUR, 3-GBP, 4-GRN, 0 - вихід): "))
        if selection == 0:
            with open(FILENAME, "w") as f:
                json.dump(bank, f)  # Збереження даних у файл перед виходом
            print("✅ Баланс збережено! 👋 На все добре!")
            break
        if selection not in range(1, 5):
            print("❌ Невірний вибір! Введіть число від 1 до 4.")
            continue

        b = float(input("Введіть новий баланс: "))
        bank[currencies[selection - 1]] += b  # Оновлення балансу

    except ValueError:
        print("❌ Некоректний ввід! Спробуйте ще раз.")

print("Оновлений баланс:", bank , "станом на", time.ctime(time.time()) )
#print('Дата останнього оновлення',time.ctime(time.time()))