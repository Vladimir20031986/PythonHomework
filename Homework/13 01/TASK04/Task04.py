# Задача №4:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


import os
os.system('cls')

def code(data):
    encoding = '' 
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else: 
        encoding += str(count) + prev_char
    return encoding


def decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open("13 01/TASK04/task04input.txt", 'r') as data:
    s = data.read()
    result = code(s)
    with open("13 01/TASK04/task04output.txt", "w") as f:
        f.write(result)
print("Текст перед кодировкой: ", s)        

with open("13 01/TASK04/task04output.txt", "r") as s:
    tocons = s.read()

print()
print(f"Текст после кодирвки:{tocons}")
print()
print(f"Текст после декодировки: {decode(tocons)}")