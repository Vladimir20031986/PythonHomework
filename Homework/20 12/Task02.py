# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
import os
os.system('cls')

s = []
for i in range(randint(2, 10)):
    s.append(randint(0, 10))

print("Случайно заданный список : ")
print()
print(s)
print()

s1 = []
for i in range(0, int(len(s)/2)):
    res = s[i] * s[len(s) - i - 1]
    s1.append(res)

print("Произведение пар чисел списка : ", s1)
