# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import os
from math import factorial
os.system('cls')

# num = int(input("Введите число: "))
# spisok = []
# result = 1
# for i in range(1, num+1):
#     result *= i
#     spisok.append(result)

# print(spisok)

n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))