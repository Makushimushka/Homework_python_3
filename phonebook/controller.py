import views
import model

def process_data():
    button = views.show_menu()
    if button == 1:
        result = model.add_contacts(views.add_contact_views())
        views.result()
    elif button == 2:
        views.display_book_views(model.read_book())
    elif button == 3:
        button_3 = views.import_export_data_view()
        filename = views.input_filename(button_3)
        model.import_txt(filename)
        if 'txt' == button_3:
            model.import_txt(filename)
        elif 'csv' == button_3:
            model.import_from_csv(filename)
        views.result()


    elif button == 4:
        button_4 = views.import_export_data_view()

        filename = views.input_filename(button_4)
        if 'txt' == button_4:
            model.export_to_txt(filename)
        elif 'csv' == button_4:
            model.export_to_csv(filename)
        views.result()

    elif button == 5:
        exit("Приложение закрыто!")


