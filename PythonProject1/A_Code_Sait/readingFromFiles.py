# Відкриваємо файл у поточному каталозі
file1 = open("testF.txt")
#print(file1.read()) # читаємо що в ньому
file_content = file1.read() # зберігаємо у змінну інфу
print(file_content,'\n') # виводимо змінну

#file1 = open("testF.txt")      # рівнозначний 'r' або 'rt'
#file1 = open("testF.txt",'w')  # запис у текстовому режимі
#file1 = open("img.bmp",'r+b') # читання та запис у двійковому режимі

file1.close()

# так правельніше
try:
    file = open("testF.txt", "r")
    read_content = file.read()
    print(read_content,'\n')

finally:
    # Закриваємо файл
    file.close()

# Оскільки в цьому варіанті не потрібно турбуватися про закриття файлу, рекомендується завжди використовувати
# синтаксис with...open
with open("testSecond.txt", "r") as file2:
    read_content2 = file2.read()
    print(read_content2,'\n')

with open("C:/Users/Admin/Desktop/Files/cat_name.txt", "r") as file5: # читання файла з діректорії на компі
    read_content5 = file5.read()
    print(read_content5,'\n')


# режим запису, якщо файл не створений створить у діректорї і запише туди інфу
with open('test2.txt', 'w') as file3:
    # Виконуємо запис у файл test2.txt
    file3.write('Programming is Fun.')
    file3.write('Python for beginners')


with open('test2.txt', 'r') as file4:
    read_content4 = file4.read(5) # прочитає вказану кількість символів
    print(read_content4,"\n")


def  reading_file(file_name): # метож приймаэ файл(директорію на компі) і повертає вміст
    with open(file_name, 'r') as file66:
        read_content66 = file66.read()
        return read_content66

name_file = "C:/Users/Admin/Desktop/Files/cat_name.txt"

print(reading_file(name_file))

# readline(): считывает одну строку из файла

# read(): считывает все содержимое файла в одну строку

# readlines(): считывает все строки файла в список



