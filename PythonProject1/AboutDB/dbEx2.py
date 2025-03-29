# NoSQL бази даних — це нереляційні системи зберігання даних, які не використовують стандартний
# SQL для обробки даних. Вони більш гнучкі, швидкі, масштабовані і здатні працювати з великими наборами даних
# та неструктурованими даними. Це робить їх популярним вибором для використання з мовами програмування,
# такими як Python.


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["university"]
collection = db["students"]


# Додаємо студентів
students = [
    {"name": "Іван Петренко", "age": 20, "course": "Computer Science"},
    {"name": "Марія Шевченко", "age": 22, "course": "Mathematics"},
    {"name": "Олег Коваленко", "age": 21, "course": "Physics"}
]

# Вставка в MongoDB
collection.insert_many(students)

for student in collection.find():
    print(student)










# Вставка даних
#user = {"name": "John", "age": 25}
#result = collection.insert_one(user)
#print(result)
# Вибірка даних
#users = collection.find()
#print(users)
# Оновлення даних
#collection.update_one({"_id": result.inserted_id}, {"$set": {"age": 26}})
# Видалення даних
#collection.delete_one({"_id": result.inserted_id})