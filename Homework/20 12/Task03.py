# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
from random import randint
import os
os.system('cls')


s = []
s1 = []
for i in range(randint(2, 10)):
    num = random.uniform(0, 10)
    s.append(round(num, 2))
    num1 = s[i] % 1
    s1.append(round(num1, 2))

print("Случайно заданный список из вещественных чисел : ")
print()
print(s)
print()
res = max(s1) - min(s1)
print("Разница между максимальным и минимальным значением дробной части : ", res)

