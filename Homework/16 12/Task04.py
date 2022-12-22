# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import os
os.system('cls')

num = int(input("Введите число: "))
spisok = []
data_from_file = []
result = 1
with open('file.txt', 'r') as data:
    for s in data:
        if s != '':
            data_from_file += [int(s)]

for i in range(-num, num + 1):
    spisok.append(i)

for i in range((len(spisok)*(-1)), len(spisok)):
    if i in data_from_file:
        result *= spisok[i]

# print(spisok)
# print(data_from_file)
print(result)