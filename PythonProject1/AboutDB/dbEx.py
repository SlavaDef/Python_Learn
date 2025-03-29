import sqlite3

connection = sqlite3.connect("my_database.db") # conection
cursor = connection.cursor()

# Виконання SQL запиту
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")


# Вставка даних
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("John", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alis", 22))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Sidni", 25))

# Вибірка даних
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)

cursor.execute("SELECT * FROM users WHERE name=?", ('Bob',))
#user = cursor.fetchone() # soose one user with name Bob
user = cursor.fetchall() # chose oll people with name Bob
print(user)



# Оновлення даних
cursor.execute("UPDATE users SET age=? WHERE id=?", (26, 1))
#print(users)
# Видалення даних
cursor.execute("DELETE FROM users WHERE id=?", (1,))


connection.commit()
connection.close()