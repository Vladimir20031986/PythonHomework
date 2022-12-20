# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os
os.system('cls')

x1 = int(input('Введите координату "Х" точки A: '))
print()
y1 = int(input('Введите координату "Y" точки A: '))
print()

x2 = int(input('Введите координату "Х" точки B: '))
print()
y2 = int(input('Введите координату "Y" точки B: '))
print()

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)

print(f"Расстояние между точками в 2D пространстве: {distance:.3f}")