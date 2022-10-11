
def show_menu():
    buttons = {1: "add",
               2: "display",
               3: "import data",
               4: "export data",
               5: "exit"}

    print("buttons: ")
    for k, v in buttons.items():
        print(f"{k}: {v}")

    while True:
        try:
            user_input = int(input("Select an action: "))
            if user_input in buttons:
                return user_input
            else:
                print("Enter correct values")
        except:
            print("Enter correct values")


def add_contact_views():
    columns = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    values = []
    for i in columns:
        values.append(str(input("Add columns '{}' : ".format(i))))

    return values

def display_book_views(data):
    print(data)





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

def result(mess = "Выполнено!"):
    print(mess)
