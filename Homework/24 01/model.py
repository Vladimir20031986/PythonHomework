import import_data as imp
import export_data as ed
from print_all_data import print_all
import pandas as pd
import time


def option():
    print("\nВас приветствует программа мониторинга процессов обучения студентов!")
    ch = int(input('Введите что хотите сделать: \n \
    1: Добавить студента\n \
    2: Поиск студента по фамилии \n \
    3: Посмотреть класс  и место которое занимает  студент \n \
    4: Выгрузить данные \n \
    5: Вывести данные в консоль \n \
    6: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        imp.add_student()
        print("Успешно!")
        time.sleep(5)
        option()

    elif ch == 2:
        Surn = str(input("Введите фамилию ученика: "))
        for i in imp.stud_card:
            if Surn in i:
                print(i)
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
    elif ch == 3:
        c = int(input('Введите ID студента для вывода по классам: '))
        print((',').join(imp.class_card[c]))
        print('\nХотите выполнить другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()
    elif ch == 4:
        ed.export_all_data()
        print("Успешно!!")
        time.sleep(5)
        option()
    elif ch == 5:
        print_all()
        time.sleep(5)
        option()
    elif ch == 6:
        print("Всего доброго!")
        time.sleep(5)
        return
    else:
        print("Вы ввели неверное значение, повторите ввод!")
        option()
    exit()