columns = ['Имя', 'Фамилия', 'Телефон', 'Описание', "Должность"]

def main_menu():
    print("_" * 70)
    buttons = {
        1: "Информация о сотрудниках",
        2: "Добавить сотрудника",
        3: "Удалить запись",
        4: "Найти информацию о сотруднике",
        5: "Изменить данные о сотруднике",
        6: "Экспортировать информацию из базу данных",
        7: "Импортировать информацию в базу данных",
        8: "Выход"
    }
    for k, v in buttons.items():
        print("{:<2}- {}".format(k,v))
    while True:
        try:
            user_input = int(input("Выберите действие: "))
            if user_input in buttons:
                return user_input
            else:
                print("Выберите значение из представленного списка")
        except:
            pass
            print("Введите в формате числа!")

def show_persons_info(data):
    for i in data:
        print(i)


def add_person_info():
    #columns = ['Имя', 'Фамилия', 'Телефон', 'Описание']
    data = {i: input("Введите {}: ".format(i.lower())) for i in columns}
    return data

def delite_person(len_data):
    while True:
        try:
            user_input = int(input("Введите индекс строки для удаления "))
            if user_input in range(len_data):
                return user_input
            else:
                print("Строки с таким номером не существует!")
        except:
            print("Введите данные в формате числа")

def find_person_menu(columns = columns):
    print("Введите информацию для поиска ")
    find_param = {i: input("{}: ".format(i)) for i in columns}
    return {k:v for k, v in find_param.items() if v != ""}

def find_person_result(num):
    if num == 0:
        print("Запись удовдетворяющая условию отсутствует!")
    else:
        print(f"Условиям поиска соответствует запись/си № {num}")


def update_person_info_menu():

    print("Меню изменений ")
    num = int(input("Введите номер строки для изменения"))
    find_param = {i: input("{}: ".format(i)) for i in columns}
    find_param = {k:v for k, v in find_param.items() if v != ""}
    return num-1, find_param

#


def import_export_data_view():
    buttons = {1: "txt",
               2: "csv"
               }
    print("buttons: ")
    for k, v in buttons.items():
        print(f"{k}: {v}")
    while True:
        try:
            user_input = int(input("Select an action: "))
            if user_input in buttons:
                return buttons[user_input]
            else:
                print("Enter correct values")
        except:
            print("Enter correct values")


def input_filename(extension):
    return str(input("Введите название файла без расширения"))+f".{extension}"



def eror_exist():
    print("База отсутствует необходимо создать либо импортировать")