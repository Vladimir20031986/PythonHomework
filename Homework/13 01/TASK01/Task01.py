# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls')

with open("13 01/TASK01/task01input.txt", "r", encoding="utf-8") as data:
    txt = data.read()
print(f"Исходный текст: {txt}")
print()
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')
with open("13 01/TASK01/task01output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(lst))