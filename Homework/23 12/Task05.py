from itertools import *
from task_4 import get_polynom
import os
os.system("cls")


file1 = 'task_4_1.txt'
file2 = 'task_4_2.txt'


def read_polinom(file):  
    with open(str(file), 'r') as data:
        polinom = data.read()
    return polinom


def convert_polinom(polinom):  
    polinom.replace('= 0', '')
    polinom = polinom.split(' + ')
    polinom = [i[0] for i in polinom]
    for i in range(len(polinom)):
        if polinom[i] == 'x':
            polinom[i] = '1'
    polinom = polinom[::-1]
    return polinom


pol1 = read_polinom(file1)
pol2 = read_polinom(file2)
print('Исходные полиномы:')
print(pol1, end='')
print(pol2)
pol1_coef = list(map(int, convert_polinom(pol1)))
pol2_coef = list(map(int, convert_polinom(pol2)))

sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
sum_coef = sum_coef[::-1]

sum_pol = get_polynom(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов:\n', sum_pol)
with open('task_5.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)