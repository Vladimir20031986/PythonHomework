from import_data import import_data
from export_data import export_data, to_txt
from print_data import print_data
from search_data import search_data
import clear
import time

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_date = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_date, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    flag = True
    while flag:
        print("Доступные операции с телефонной книгой:\n\
        1 - Новый контакт\n\
        2 - Вывести данные в консоль и в txt\n\
        3 - Поиск в телефонной книге\n\
        4 - Очистить телефонную книгу\n\
        5 - Выход")
        ch = input("Введите цифру: ")
        if ch == '1':
            sep = choice_sep()
            import_data(input_data(), sep)
            print('Выполнено успешно!')
        elif ch == '2':
            data = export_data()
            to_txt()
            print_data(data)
            time.sleep(5)
        elif ch == '3':
            word = input("Введите данные для поиска: ")
            data = export_data()
            item = search_data(word, data)
            if item != None:
                print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
                print("-"*130)
                print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
                time.sleep(5)
            else:
                print("Данные не обнаружены")
                time.sleep(5)
        elif ch == '4':
            clear.clear_phone()
            print("Выполнено успешно!")
            time.sleep(5)
        elif ch == '5':
            flag = False
        else:
            print("Вы ввели некорректное значение! Повторите ввод!")
            time.sleep(5)