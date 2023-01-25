import json
import codecs
import unicodedata


def export_data():
    with open('phone.csv', 'r') as file:
        data = []
        titles = []
        t = []
        for line in file:
            if file == None:
                data.append(titles)
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.strip().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.strip().split(':')
                data.append(temp)        
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []
    return data

def to_txt():
    with open('phone.csv', 'r') as f_in, open('phone.txt', 'w') as f_out:
        content = f_in.read()
        f_out.write(content)