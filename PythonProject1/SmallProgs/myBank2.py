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
conn.commit()

# Завантаження даних у словник
cur.execute("SELECT * FROM bank")
bank = dict(cur.fetchall())

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

        b = float(input("Введіть новий баланс: "))
        currency = currencies[selection - 1]
        bank[currency] = b

        # Оновлення балансу у базі
        cur.execute("UPDATE bank SET balance = ? WHERE currency = ?", (b, currency))

    except ValueError:
        print("❌ Некоректний ввід! Спробуйте ще раз.")