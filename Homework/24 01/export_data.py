from import_data import *
import pandas as pd
 
def export_all_data():
    sc = pd.DataFrame(data = stud_card)
    cc = pd.DataFrame(data = class_card)
    with open('students.csv', 'w', encoding='UTF-8') as student_data:
        student_data.write(f'{sc}')
        student_data.write('\n')
    with open('classes.csv', 'w', encoding='UTF-8') as class_data:
        class_data.write(f'{cc}')
        class_data.write('\n')