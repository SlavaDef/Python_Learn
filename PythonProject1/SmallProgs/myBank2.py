import sqlite3

# Підключення до бази даних (створиться файл bank.db)
conn = sqlite3.connect("bank.db")
cur = conn.cursor()

# Створення таблиці, якщо її ще немає
cur.execute("""
CREATE TABLE IF NOT EXISTS bank (
    currency TEXT PRIMARY KEY,
    balance REAL
)
""")

# Початкові значення (вставляються тільки якщо валюта ще не додана)
default_balances = {'USD': 10927, 'EUR': 3800, 'GBP': 30, 'GRN': 30}
for currency, balance in default_balances.items():
    cur.execute("INSERT OR IGNORE INTO bank (currency, balance) VALUES (?, ?)", (currency, balance))
    # якщо таблиця пуста то витягуємо данні з дефолт словника та вставляємо їх в бд
conn.commit()
# INSERT OR IGNORE преобразует ошибку в предупреждение. При этом выполнение запроса продолжается, а запись,
# попытка вставки которой привела к ошибке, не вставляется

# Завантаження даних у словник
cur.execute("SELECT * FROM bank")
bank = dict(cur.fetchall()) # оскільки два столбця то створить новий словник з данними з бд

print("Початковий баланс:", bank)

currencies = ['USD', 'EUR', 'GBP', 'GRN']

while True:
    try:
        selection = int(input("Виберіть валюту (1-USD, 2-EUR, 3-GBP, 4-GRN, 0 - вихід): "))
        if selection == 0:
            conn.commit()  # Збереження змін у базі даних
            conn.close()
            print("✅ Баланс збережено у базі! 👋 На все добре!")
            break
        if selection not in range(1, 5):
            print("❌ Невірний вибір! Введіть число від 1 до 4.")
            continue

        b = float(input("Введіть новий баланс: ")) # отримали нову суму
        currency = currencies[selection - 1] # ключ = данні з масиву(currencies) -1 (якщо 1 то 0)
        bank[currency] = b # словник з таким то ключем отримає нову сумму

        # Оновлення балансу у базі
        cur.execute("UPDATE bank SET balance = ? WHERE currency = ?", (b, currency))

    except ValueError:
        print("❌ Некоректний ввід! Спробуйте ще раз.")