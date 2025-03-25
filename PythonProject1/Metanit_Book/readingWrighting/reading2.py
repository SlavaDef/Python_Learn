name_file = "C:/Users/Admin/Desktop/Files/cat_name.txt"

with open(name_file, 'r') as file:
    contents = file.readlines() # створить масив строк з вмісту файлу
    print(contents)


filename = "C:/Users/Admin/Desktop/GIT.txt"
with open(filename, encoding="utf8") as file: # для чтання латиниці вказується кодіровка
    text = file.read()
    print(text)

# Аналогичным образом мы можем перемещаться по файлу на нужную позицию.Например,
# считаем данные, начиная с 5 - го символа:
print('-----------------------------------------------------------------------------------------------------')

with open("../../A_Code_Sait/test3.txt", "w+") as file:
    file.write("Hello world\n")  # сначала записываем данные
    file.seek(6)  # перемещаемся к шестому байту в файле
    content = file.read()  # считываем данные
    print(content)  # world