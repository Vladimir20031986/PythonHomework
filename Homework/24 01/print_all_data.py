import pandas as pd
from import_data import stud_card, class_card

def print_all():
    print('----'*30)
    print('Список учеников')
    sc = pd.DataFrame(data = stud_card)
    print(sc)
    print('----'*30)
    print('Информация о классах')   
    cc = pd.DataFrame(data = class_card)
    print(cc)