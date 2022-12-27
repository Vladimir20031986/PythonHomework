# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


import os
os.system('cls')

myList = list(map(int, input("Введите числа через пробел: ").split()))
print()
print(f"Исходный список: {myList}")
newList = []
[newList.append(i) for i in myList if i not in newList]
print()
print(f"Список из неповторяющихся элементов: {newList}")