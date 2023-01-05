# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from itertools import *
from random import randint
import os
os.system("cls")


k = randint(2, 7)  # случайным образом выбираем степень
print('k = ', k)


def get_new_list(k):  # заполняем массив ratios случайными числами, чтобы первый элемент был не нулевой
    my_list = [randint(1, 9) for i in range(k + 1)]
    while my_list[0] == 0:
        my_list[0] = randint(1, 9)
    return my_list


def get_polynom(k, my_list):  # вычисляем полином, передаем степень и массив коэффициентов
    i = ['*x^']*(k-1) + ['*x']
    polynom = [[a, b, c] for a, b, c in zip_longest(
        my_list, i, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynom:
        x.append(' + ')
    polynom = list(chain(*polynom))
    polynom[-1] = ' = 0'
    return "".join(map(str, polynom)).replace(' 1*x', ' x')


my_list = get_new_list(k)
polynom1 = get_polynom(k, my_list)
print(polynom1)

# перезаписываем результат в файл1, предыдущая запись обнуляется
with open('task_4_1.txt', 'w') as data:
    data.writelines(polynom1)
    data.writelines('\n')


# Второй многочлен для следующей задачи:

k = randint(2, 5)

my_list_2 = get_new_list(k)
polynom2 = get_polynom(k, my_list)
print(polynom2)

with open('task_4_2.txt', 'w') as data:  # добавляем запись в файл
    data.write(polynom2)