# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


import os
os.system('cls')

x = int(input("Введите любое натуральное число: "))

n = bin(x)
print()
print("Вид введенного числа в двоичной системе счисления :", n)

