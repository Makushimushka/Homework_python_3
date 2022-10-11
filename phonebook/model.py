import pandas as pd
import os

def add_contacts(data):
    columns = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    if os.path.exists('phonebook.csv'):
        with open('phonebook.csv', 'a') as file:
            file.write(';'.join(data) + "\n")
    else:
        with open('phonebook.csv', 'w') as file:
            file.write(';'.join(columns) + "\n")
            file.write(';'.join(data) + "\n")


def read_book():
    #return '; '.join(data) + ";\n"
    try:
        df = pd.read_csv('phonebook.csv', sep = ';')
        return df
    except:
        return False


def import_txt(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            file = file.readlines()
            file = list(map(lambda x: x.replace('\n', ';'), file))
            for i in range(3, len(file), 4):
                file[i] = file[i].replace(';', '\n')
            with open('phonebook.csv', "w") as f:
                print(''.join(file[:-1]), file=f)

def import_from_csv(file_name):
    with open(file_name, 'r') as file:
        file = file.readlines()

    with open('phonebook.csv', "w") as f:
        print(''.join(file), file=f)


def export_to_txt(file_name):
    with open('phonebook.csv', 'r') as file:
        file = ''.join(file.readlines())
        file = file.replace(';', '\n')

    with open(file_name, "w") as f:
        print(file, file=f)

def export_to_csv(file_name):
    with open('phonebook.csv', 'r') as file:
        file = file.readlines()

    with open(file_name, "w") as f:
        print(''.join(file), file=f)