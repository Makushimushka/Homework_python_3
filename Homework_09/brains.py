import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd



con = sqlite3.connect('db.db', check_same_thread=False)
curs = con.cursor()
try:
    curs.execute("CREATE TABLE phoneboock (id INTEGER PRIMARY KEY, Фамилия text, Имя text, Отчество text, Телефон text, Комментарий text)")
    con.commit()
except:
    print("Уже существует")

def add_values(data):
    values = [x for x in data.values()]
    #print(values)
    curs.execute(
        "insert into phoneboock (Фамилия, Имя, Отчество, Телефон, Комментарий) values ('{}', '{}', '{}', '{}', '{}')".format(
            values[0], values[1], values[2], values[3], values[4]
        ))
    con.commit()

def show_b():
    curs.execute("select * from phoneboock")
    results = ""
    for i in curs.fetchall():
        results = results + '|{:<2}|{:<10}|{:<10}|{:<11}|{:<15}|\n'.format(i[0], i[1], i[2], i[3], i[4])
    return results

# поиск записи
def find_b(data):
    get_find = ''
    index = 0
    for k, v in data.items():
        if index == 0:
            get_find = f"select * from phoneboock where " + f"{k}" + " like " + f"'{v}'"
            index += 1
        else:
            get_find = get_find + " and " + f"{k}" + " like " + f"'{v}'"
    curs.execute(get_find)
    results = ""
    for i in curs.fetchall():
        results = results + '|{:<3}|{:<10}|{:<10}|{:<11}|{:<15}|\n'.format(i[0], i[1], i[2], i[3], i[4])
    return results



def delete_val_b(id):
    curs.execute(f"delete from phoneboock where id={id}")
    con.commit()


def update_info(id, data):
    print(id, data)
    get_find = ''
    for k, v in data.items():
        get_find = f"update phoneboock set {k} = '{v}' where id = {id}"
        curs.execute(get_find)
        con.commit()