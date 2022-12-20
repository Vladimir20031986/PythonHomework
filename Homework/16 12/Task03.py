# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


import os
os.system('cls')

num = int(input("Введите число: "))
res1 = {}
res2 = []
x = 0

for i in range(1, num + 1):
    x = round((1+1/i)**i, 2)
    res1[i] = x
    res2.append(x)

print(res1)
print(res2)