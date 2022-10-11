import view
import model


def process_data():
    button = view.main_menu()
    if button == 1:
        # "Информация о сотрудниках"
        view.show_persons_info(model.get_db())
    elif button == 2:
        # "Добавить сотрудника"
        model.add_person(view.add_person_info())
    elif button == 3:
        model.delite_row(view.delite_person(len(model.get_db())))
    elif button == 4:
        #"Найти информацию о сотруднике"
        result = model.find_person(view.find_person_menu())
        view.find_person_result(result)
    elif button == 5:
        temp = view.update_person_info_menu()
        model.update_row(temp[0], temp[1])
        pass
        #"Изменить данные о сотруднике"
    elif button == 6:
        filename = view.input_filename(view.import_export_data_view())
        if "csv" in filename:
            model.export_csv(filename)
        if 'txt' in filename:
            model.export_to_txt(filename)
        #"Экспортировать информацию из базы данных"
    elif button == 7:
        # "Импортировать информацию в базу данных"}
        filename = view.input_filename(view.import_export_data_view())
        if "csv" in filename:
            model.import_from_csv(filename)
        if 'txt' in filename:
            model.import_txt(filename)


    elif button == 8:
        exit("Выход")
        # "Экспортировать информацию в базу данных"}
