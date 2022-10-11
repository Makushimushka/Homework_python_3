import csv
import os
import pandas as pd

import view

PATH_BD = 'bd.csv'

def add_person(data):
    columns = data.keys()
    exist = os.path.exists(PATH_BD)
    with open(PATH_BD, 'a', encoding= "utf-8") as file:
        file_writer = csv.DictWriter(file, delimiter = ";", fieldnames = columns, lineterminator="\r")
        if not exist:
            file_writer.writeheader()
            file_writer.writerow(data)
        else:
            file_writer.writerow(data)

def get_db():
    if not os.path.exists(PATH_BD):
        view.eror_exist()
        exit()
    else:
        with open(PATH_BD, 'r', encoding= "utf-8") as file:
            file_reader = csv.DictReader(file, delimiter = ";", lineterminator="\r")
            result = []
            #return (pd.read_csv(PATH_BD, delimiter = ";"))
            columns = file_reader.fieldnames
            result.append(''.join(["{:<15}".format(i) for i in columns]))
            for row in file_reader:
                print_form = ''.join(["{:<15}".format(row[i]) for i in row])
                result.append((print_form))
            result = ["{:<4}".format(str(i[0])) + str(i[1]) for i in enumerate(result)]
        return result

def delite_row(num_row):

    with open(PATH_BD, 'r', encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=";", lineterminator="\r")
        new_list = list(file_reader)
        new_list.pop(num_row - 1)

    with open(PATH_BD, 'w', encoding="utf-8") as file:
        columns = list(new_list[0].keys())
        file_writer = csv.DictWriter(file, delimiter=";", fieldnames=columns, lineterminator="\r")
        file_writer.writeheader()
        file_writer.writerows(new_list)

def find_person(find_param):
    with open(PATH_BD, 'r', encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=";", lineterminator="\r")
        flag = True
        index = 1
        result_list = []
        for row in file_reader:
            result = [row[k] == v for k, v in find_param.items()]
            if False in result:
                index+=1
            else:
                result_list.append(index)
                index += 1
    return result_list


def update_row(num_row, data):

    with open(PATH_BD, 'r', encoding="utf-8") as file:
        file_reader = csv.DictReader(file, delimiter=";", lineterminator="\r")
        new_list = list(file_reader)

        for k,v in data.items():
            new_list[num_row][k] = v

    with open(PATH_BD, 'w', encoding="utf-8") as file:
        columns = list(new_list[0].keys())
        file_writer = csv.DictWriter(file, delimiter=";", fieldnames=columns, lineterminator="\r")
        file_writer.writeheader()
        file_writer.writerows(new_list)


def export_csv(file_name):

    with open(PATH_BD, 'r', encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter=";", lineterminator="\r")
        with open(file_name, 'w', encoding="utf-8") as file:
            file_writer = csv.writer(file, delimiter=";",  lineterminator="\r")
            file_writer.writerows(file_reader)


def import_from_csv(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        file_reader = csv.reader(file, delimiter=";", lineterminator="\r")
        with open(PATH_BD, 'w', encoding="utf-8") as file:
            file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
            file_writer.writerows(file_reader)


def export_to_txt(file_name):
    with open('bd.csv', 'r') as file:
        file = ''.join(file.readlines())
        file = file.replace(';', '\n')

    with open(file_name, "w") as f:
        print(file, file=f)



def import_txt(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            file = file.readlines()
            file = list(map(lambda x: x.replace('\n', ';'), file))
            for i in range(3, len(file), 4):
                file[i] = file[i].replace(';', '\n')
            with open(PATH_BD, "w") as f:
                print(''.join(file[:-1]), file=f)

