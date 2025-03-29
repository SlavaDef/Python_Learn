import sqlite3

connection = sqlite3.connect("users_database.db") # conection
cursor = connection.cursor()


# Создаем таблицу Users

def create_table():
    return cursor.execute('''
CREATE TABLE IF NOT EXISTS Users2 (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')

def insert_data(name, email, age):
    cursor.execute('INSERT INTO Users2 (username, email, age) VALUES (?, ?, ?)',
                   (name, email, age))

# Обновляем возраст пользователя "newuser"
def update_age(age, name):
    cursor.execute('UPDATE Users2 SET age = ? WHERE username = ?', (age, name))


 # cursor.execute('CREATE INDEX idx_email ON Users2 (email)')

def find_all():
    cursor.execute("SELECT * FROM Users2")
    users = cursor.fetchall()
    print(users)


def delete_user(name):
    cursor.execute('DELETE FROM Users2 WHERE username = ?', (name,))

# Выбираем имена и возраст пользователей старше ... лет
def find_user_by_age(age):
    cursor.execute('SELECT username, age FROM Users2 WHERE age > ?', (age,))
    results = cursor.fetchall()

    for row in results:
        print(row)


# Получаем средний возраст пользователей для каждого возраста
def average_age():
    cursor.execute('SELECT age, AVG(age) FROM Users2 GROUP BY age')
    results = cursor.fetchall()

    for row in results:
        print(row)

# Фильтруем группы по среднему возрасту больше 30
def filter_by_age(age):
    cursor.execute('SELECT age, AVG(age) FROM Users2 GROUP BY age HAVING AVG(age) > ?', (age,))
    filtered_results = cursor.fetchall()
    for row in filtered_results:
        print(row)



#create_table()
#insert_data("newuser66", "<EMAIL>", 25)
#insert_data("newuser67", "user@gmail.com", 30)
#insert_data("newuser55", "user55@gmail.com", 18)
#insert_data("newuser54", "user54@gmail.com", 20)
#insert_data("newuser53", "user53@gmail.com", 21)

find_all()
#update_age(88, "newuser66")
#find_all()
#delete_user("newuser67")
#find_user_by_age(19)
#average_age()
filter_by_age(30)

#find_all()


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

