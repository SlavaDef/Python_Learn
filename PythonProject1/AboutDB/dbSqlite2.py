#Триггеры - это специальные хранимые процедуры, которые автоматически вызываются при изменении данных в таблице.
# Давайте создадим триггер для автоматического обновления времени создания пользователя:

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database22.db')
cursor = connection.cursor()

# Создаем таблицу Users22
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users22 (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

# Создаем триггер для обновления времени создания при вставке новой записи
cursor.execute('''
CREATE TRIGGER IF NOT EXISTS update_created_at
AFTER INSERT ON Users22
BEGIN
UPDATE Users22 SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
''')

# cursor.execute('INSERT INTO Users22 (username, email, age) VALUES (?, ?, ?)', ('John', 'user@gmail.com', 25))

# Создаем индекс для столбца "username"
cursor.execute('CREATE INDEX IF NOT EXISTS idx_username ON Users22 (username)')



def create_user22(name, email, age):
    try:
        # Починаємо транзакцію
        cursor.execute('BEGIN')

        # Виконуємо інсерти
        cursor.execute('INSERT INTO Users22 (username, email, age) VALUES (?, ?, ?)', (name, email, age))

        # Підтверджуємо зміни
        cursor.execute('COMMIT')

    except:
        # Якщо помилка, то скасування транзакції
        cursor.execute('ROLLBACK')



def find_all22():
    cursor.execute("SELECT * FROM Users22")
    users = cursor.fetchall()
    print(users)


create_user22("Jesika_P", "jessi2005@gmail.com", 20)
find_all22()


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()