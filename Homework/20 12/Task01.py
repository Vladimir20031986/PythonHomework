# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import os
os.system('cls')

from random import randint

s = []
for i in range(10):
    s.append(randint(0, 10))
print("Случайно заданный список : ")
print()
print(s)
print()
sum = 0
for i in range(len(s)): 
    if i%2 !=0:
        sum += s[i]

print("Cумма элементов списка, стоящих на нечётной позиции : ", sum)

