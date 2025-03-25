
directory = "C:/Users/Admin/Desktop/Files/cat_name22.txt"
w = 'w' # запис
r = 'r' # читання
a = 'a' # до запис

def writing_file(name_file, met = 'w'):
    # метод запише і створить файл з імям і вмістом на компі
    with open(name_file, met) as file:
        # Виконуємо запис у файл test2.txt
        file.write('Programming is Fun.\n')
        file.write('Python for beginners\n')
        file.write('Hello Erick\n')


# writing_file(directory)
# writing_file(directory, a) # дозапис

lines = ["Hello Word\n", "Hello Work\n", "Hello World\n"]
with open(directory, "a") as file: # дозапис масиву строк з методом writelines
    file.writelines(lines)

print("Список строк записан в файл")
