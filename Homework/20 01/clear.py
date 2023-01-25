def clear_phone():
    with open("phone.csv", "w") as file, open("phone.txt", 'w') as file2:
        file.write('')
        file2.write('')

clear_phone()
