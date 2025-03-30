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


def find_user_by_id(ids):
    cursor.execute('SELECT username, email, age FROM Users2 WHERE id = ?', (ids,))
    results = cursor.fetchone()
    return results




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


# Выбираем и сортируем пользователей по возрасту по убыванию
def order_by_age():
    cursor.execute('SELECT username, age FROM Users2 ORDER BY age DESC')
    results = cursor.fetchall()
    print(results)


# Выбираем и сортируем пользователей по возрасту по убыванию в группе больше 30
def having_avg_order_by_age(age=30):
    cursor.execute('''
    SELECT username, age, AVG(age)
    FROM Users2
    GROUP BY age
    HAVING AVG(age) > ?
    ORDER BY age DESC
    ''', (age,))
    results = cursor.fetchall()
    print(results)


# Подсчет общего числа пользователей
def user_count():
    cursor.execute('SELECT COUNT(*) FROM Users2')
    count = cursor.fetchone()[0]
    print('Общее количество пользователей:',count)


# Вычисление суммы возрастов пользователей
def sum_of_the_ages():
    cursor.execute('SELECT SUM(age) FROM Users2')
    total_age = cursor.fetchone()[0]

    print('sum_of_the_ages of users is ', total_age)


# Вычисление среднего возраста пользователей
def avg_users_ages():
    cursor.execute('SELECT AVG(age) FROM Users2')
    average_age2 = cursor.fetchone()[0]

    print('AVG age of users is ', average_age2)

# знаходження мін age / or max
def min_age():
    cursor.execute('SELECT MIN(age) FROM Users2')
    min_age2 = cursor.fetchone()[0]
    print('min age =', min_age2)


def fetch_some_data():
    # Выбираем первого пользователя
    cursor.execute('SELECT * FROM Users2')
    first_user = cursor.fetchone()
    print(first_user)

    # Выбираем первых 5 пользователей
    cursor.execute('SELECT * FROM Users2')
    first_five_users = cursor.fetchmany(5)
    print(first_five_users)

    # Выбираем всех пользователей
    cursor.execute('SELECT * FROM Users2')
    all_users = cursor.fetchall()
    print(all_users)


# преобразуем результаты запроса на выборку всех пользователей в список словарей

def fetch_all_users_as_dict():
    # достаємо всіх юзерів
    cursor.execute('SELECT * FROM Users2')


    users = cursor.fetchall()
    res = {}
    i = 0
    for user in users:
        if i > len(users)-1:
            break
        res[i]=user
        i += 1
    return res


def null_age():
    cursor.execute('SELECT * FROM Users2 WHERE age IS NULL')
    null_age2 = cursor.fetchall()
    print(null_age2)


# більш надійний спосіб створення
# управління транзакціями в SQLite
def create_user(name, email, age):
    try:
        # Починаємо транзакцію
        cursor.execute('BEGIN')

        # Виконуємо інсерти
        cursor.execute('INSERT INTO Users2 (username, email, age) VALUES (?, ?, ?)', (name, email, age))
        # cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (name, email, age))

        # Підтверджуємо зміни
        cursor.execute('COMMIT')

    except:
        # Якщо помилка, то скасування транзакції
        cursor.execute('ROLLBACK')



#create_table()
#insert_data("newuser66", "<EMAIL>", 25)
#insert_data("newuser67", "user@gmail.com", 30)
#insert_data("newuser55", "user55@gmail.com", 18)
#insert_data("newuser54", "user54@gmail.com", 20)
#insert_data("Bob", "Bobby33@gmail.com", 33)

find_all()
#update_age(88, "newuser66")
#find_all()
#delete_user("newuser66")

#find_user_by_age(19)
#average_age()
#filter_by_age(30)
#order_by_age()
#find_all()
#having_avg_order_by_age()
#user_count()
#sum_of_the_ages()
#avg_users_ages()
#min_age()
#fetch_some_data()
#null_age()
#create_user("BabaNata", "BabaNata@gmail.com", 92)


#print(fetch_all_users_as_dict()[2])

res = find_user_by_id(8)
print('name = ',res[0], ', email = ',res[1], ', age = ',res[2],sep='')





# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

