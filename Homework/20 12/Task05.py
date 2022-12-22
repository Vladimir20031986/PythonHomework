# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


import os
os.system('cls')

x = int(input("Введите любое натуральное число: "))

a, b = 0, 1
s = []
s.append(a)
s.append(b)

for i in range(x - 1):
    fib = a + b
    s.append(fib)
    a = b
    b = fib

a, b = 0, 1

for i in range(x):
    negfib = b - a
    s.insert(0, negfib)
    b = a
    a = negfib
print()
print('Список чисел Фибоначчи, в том числе для отрицательных индексов: ')
print()
print(s)
