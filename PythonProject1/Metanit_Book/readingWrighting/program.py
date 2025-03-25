# имя файла
#FILENAME = "messages.txt"
#directory = "C:/Users/Admin/Desktop/Files/cat_name66.txt"
directory = 'cat_name66.txt'


def write_message():
    text = input("Залиште Ваше повідомлення абоненту: ")
    with open(directory, "a", encoding="utf-8") as file: # а - це дозапис
        file.writelines(text + "\n")

    print("Ваше повідомлення записане ")


def read():
    with open(directory, "r") as file:
        print('Прослуховування повідомлення:')
        for message in file:
            print(message, end="")
    print() # перевод строки для разделения меню и вывода



def  reading_file(): # метож приймаэ файл(директорію на компі) і повертає вміст
    try:
        with open(directory, 'r', encoding="utf-8") as file:
           read_content = file.read()
           print(read_content)
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку запишіть повідомлення.")


while True:
    print("1. Запис до файлу\t2. Читання повідомлення\t3. Вихід")
    selection = input("Зробіть вибір: ")
    # Проверяем, является ли ввод числом
    # continue — оператор, который прерывает текущую итерацию и возвращает программу в начало цикла.
    # То есть, если ввод неправильный, программа снова предложит сделать выбор.
    if not selection.isdigit():
        print()
        print("Кривий ввід. Введіть число від 1 до 3.")
        continue

        # Преобразуем в число
    selection = int(selection)

    match selection:
        case 1:
            write_message()
        case 2:
            reading_file()
        case 3:
            break
        case _:
            print("Кривий ввід")

print("Кінець проги")

