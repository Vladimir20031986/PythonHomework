# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('cls')

num = float(input("Введите число: "))
a = list(str(num))
print()
sum = 0
for i in a:
    if i.isdigit():
        sum += int(i)
print("Сумма цифр введенного числа : ", sum)
