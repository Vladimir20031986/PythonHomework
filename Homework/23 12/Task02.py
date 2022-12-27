# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


import os
os.system('cls')

x = int(input("Введите число: "))
i = 2 
s = []
num = x
while i <= x:
    if x % i == 0:
        s.append(i)
        x //= i
        i = 2
    else:
        i += 1
print()
print(f"Простые множители числа {num}: {s}")